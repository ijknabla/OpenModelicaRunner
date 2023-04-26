import re
import socket
import sys
from asyncio import Task, get_running_loop
from collections.abc import Callable, Coroutine, Iterator
from contextlib import closing
from dataclasses import dataclass
from functools import wraps
from getpass import getuser
from pathlib import Path
from tempfile import gettempdir
from typing import TYPE_CHECKING, Any, ParamSpec, TypeVar, cast

from PySide6.QtCore import Slot

if TYPE_CHECKING:
    from typing_extensions import Self
_P = ParamSpec("_P")
_T = TypeVar("_T")


def find_free_port() -> int:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("localhost", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return cast(int, s.getsockname()[1])


def bg(f_co: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, Task[_T]]:
    @wraps(f_co)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> Task[_T]:
        loop = get_running_loop()
        task = loop.create_task(f_co(*args, **kwargs))
        task.add_done_callback(_done_callback)
        return task

    return wrapper


def AsyncSlot(
    *args0: Any, **kwargs0: Any
) -> Callable[[Callable[_P, Coroutine[Any, Any, _T]]], Callable[_P, None]]:
    def decorator(f: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, None]:
        @Slot(*args0, **kwargs0)
        @wraps(f)
        def wrapper(*args1: _P.args, **kwargs1: _P.kwargs) -> None:
            loop = get_running_loop()
            task = loop.create_task(f(*args1, **kwargs1))
            task.add_done_callback(_done_callback)

        return cast(Callable[_P, None], wrapper)

    return decorator


def _done_callback(task: Task[_T]) -> None:
    try:
        task.result()
    except Exception:
        sys.excepthook(*sys.exc_info())


def get_omedit_work_directory() -> Path:
    if sys.platform == "win32":
        return Path.home() / "AppData" / "Local" / "Temp" / "OpenModelica" / "OMEdit"
    else:
        return Path(gettempdir()) / f"OpenModelica_{getuser()}" / "OMEdit"


@dataclass
class BuiltModel:
    executable: Path
    init_xml: Path
    info_json: Path

    @property
    def directory(self) -> Path:
        return self.executable.parent

    @classmethod
    def from_directory(cls, directory: Path) -> Iterator["Self"]:
        init_xml_stems = set(
            re.sub(r"_init\.xml$", "", path.name) for path in directory.glob("*_init.xml")
        )
        info_json_stems = set(
            re.sub(r"_info\.json$", "", path.name) for path in directory.glob("*_info.json")
        )
        stems = init_xml_stems & info_json_stems

        for stem in stems:
            for name in f"{stem}.exe", stem:
                executable = directory / name
                if executable.exists():
                    break
            else:
                continue

            init_xml = directory / f"{stem}_init.xml"
            info_json = directory / f"{stem}_info.json"

            yield cls(executable=executable, init_xml=init_xml, info_json=info_json)

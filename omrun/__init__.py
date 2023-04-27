import re
import sys
from asyncio import Task, create_task, get_running_loop
from asyncio.exceptions import CancelledError
from collections.abc import AsyncGenerator, AsyncIterator, Callable, Coroutine, Iterator
from contextlib import asynccontextmanager, suppress
from dataclasses import dataclass
from functools import partial, wraps
from getpass import getuser
from pathlib import Path
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket
from tempfile import gettempdir
from typing import TYPE_CHECKING, Any, AnyStr, ParamSpec, TypeVar, cast

from PySide6.QtCore import Slot

if TYPE_CHECKING:
    from typing_extensions import Self
_P = ParamSpec("_P")
_T = TypeVar("_T")


def find_free_port() -> int:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        return cast(int, s.getsockname()[1])


@asynccontextmanager
async def listen_port(
    port: int,
    callback: Callable[
        [Callable[[int], Coroutine[None, None, bytes]]], Coroutine[None, None, None]
    ],
) -> AsyncGenerator[None, None]:
    with socket(AF_INET, SOCK_STREAM) as server:
        server.setblocking(False)
        server.bind(("localhost", port))
        server.listen()

        async def serve() -> None:
            loop = get_running_loop()
            while True:
                client, _ = await loop.sock_accept(server)
                with client:
                    client.setblocking(False)
                    await create_task(callback(partial(loop.sock_recv, client)))

        serve_task = create_task(serve())
        try:
            yield None
        finally:
            serve_task.cancel()
            with suppress(CancelledError):
                await serve_task


async def readlines(
    read: Callable[[], Coroutine[Any, Any, AnyStr]], keepends: bool = False
) -> AsyncIterator[AnyStr]:
    data: AnyStr | None = None
    async for new_data in _readchunks(read):
        if data is None:
            data = new_data
        else:
            data += new_data

        *lines, data = data.splitlines(keepends=keepends)
        for line in lines:
            yield line  # type: ignore

    yield data  # type: ignore


async def _readchunks(read: Callable[[], Coroutine[Any, Any, AnyStr]]) -> AsyncIterator[AnyStr]:
    data = await read()
    while data:
        yield data
        data = await read()


def AsyncSlot(
    *args: Any, **kwargs: Any
) -> Callable[[Callable[_P, Coroutine[Any, Any, _T]]], Callable[_P, Task[_T]]]:
    def decorator(f: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, Task[_T]]:
        return cast(Callable[_P, Task[_T]], Slot(*args, **kwargs)(bg(f)))

    return decorator


def bg(f_co: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, Task[_T]]:
    @wraps(f_co)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> Task[_T]:
        loop = get_running_loop()
        task = loop.create_task(f_co(*args, **kwargs))
        task.add_done_callback(_done_callback)
        return task

    return wrapper


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

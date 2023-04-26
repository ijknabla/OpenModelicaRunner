import sys
from asyncio import Task, get_running_loop
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeVar, cast

from PySide6.QtCore import Slot

_P = ParamSpec("_P")
_T = TypeVar("_T")


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

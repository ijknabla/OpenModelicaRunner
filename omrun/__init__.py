from asyncio import run
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeVar

_P = ParamSpec("_P")
_T = TypeVar("_T")


def unasync(f: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, _T]:
    @wraps(f)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        return run(f(*args, **kwargs))

    return wrapper

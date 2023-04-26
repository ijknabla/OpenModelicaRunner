import sys
from typing import Any

from PySide6.QtWidgets import QApplication
from typing_extensions import Self

class _QEventLoop:
    def __init__(
        self,
        app: QApplication | None = ...,
        set_running_loop: bool = ...,
        already_running: bool = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Any) -> None: ...

from ._unix import _SelectorEventLoop  # noqa

class QSelectorEventLoop(_QEventLoop, _SelectorEventLoop): ...

if sys.platform == "win32":
    from ._windows import _ProactorEventLoop

    class QIOCPEventLoop(_QEventLoop, _ProactorEventLoop): ...
    QEventLoop = QIOCPEventLoop
else:
    QEventLoop = QSelectorEventLoop

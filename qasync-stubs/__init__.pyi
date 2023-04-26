import os
from typing import Any

from PySide6.QtWidgets import QApplication
from typing_extensions import Self

from ._unix import _SelectorEventLoop

class _QEventLoop:
    def __init__(
        self,
        app: QApplication | None = ...,
        set_running_loop: bool = ...,
        already_running: bool = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Any) -> None: ...

class QSelectorEventLoop(_QEventLoop, _SelectorEventLoop): ...

if os.name == "nt": ...
else:
    QEventLoop = QSelectorEventLoop

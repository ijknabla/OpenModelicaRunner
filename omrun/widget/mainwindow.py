import re
from asyncio import create_subprocess_exec
from collections.abc import Callable, Coroutine
from functools import partial
from pathlib import Path
from typing import ClassVar

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QListWidgetItem, QMainWindow, QProgressBar, QWidget

from .. import BuiltModel, bg, find_free_port, get_omedit_work_directory, listen_port, readlines
from ..ui.mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    progressUpdated: ClassVar[Signal] = Signal(int, int, str)
    workDirectoryUpdated: ClassVar[Signal] = Signal(Path)
    progressBars: dict[int, QProgressBar]

    def __init__(
        self,
        parent: QWidget | None = None,
        flags: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.workDirectoryUpdated.connect(self.modelBrowser.workDirectoryChanged.emit)
        self.progressUpdated.connect(self.on_progressUpdated)
        self.progressBars = {}
        self.showMaximized()

        self.workDirectoryUpdated.emit(get_omedit_work_directory())
        self.modelBrowser.modelSelected.connect(bg(self.run_clicked))

    def on_progressUpdated(self, port: int, progress: int, status: str) -> None:
        match status:
            case "Starting":
                item = QListWidgetItem()
                bar = QProgressBar()
                self.processWidget.addItem(item)
                self.processWidget.setItemWidget(item, bar)
                self.progressBars[port] = bar
            case "Running":
                bar = self.progressBars[port]
            case "Finished":
                bar = self.progressBars[port]
            case _:
                raise NotImplementedError()
        bar.setValue(progress)

    async def run_clicked(self, builtmodel: BuiltModel) -> None:
        port = find_free_port()
        async with listen_port(port, partial(self.handle_progress, port)):
            await run_builtmodel(builtmodel, port)

    async def handle_progress(
        self, port: int, read: Callable[[int], Coroutine[None, None, bytes]]
    ) -> None:
        async for line in readlines(partial(read, 1024)):
            for match in re.finditer(
                r"(?P<progress>\d+) (?P<status>[a-zA-Z]+)", line.decode("utf-8")
            ):
                progress = 100 * int(match.group("progress")) // 10000
                status = match.group("status")
                self.progressUpdated.emit(port, progress, status)


async def run_builtmodel(builtmodel: BuiltModel, port: int | None = None) -> None:
    port_option = () if port is None else (f"-port={port}",)

    process = await create_subprocess_exec(
        f"{builtmodel.executable}", *port_option, cwd=builtmodel.directory
    )
    await process.wait()
    print(f"{builtmodel.executable} done!")

from pathlib import Path

import click
from PySide6.scripts.pyside_tool import qt_tool_wrapper


@click.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.argument(
    "ui_paths",
    metavar="[UI]...",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    nargs=-1,
)
def main(
    directory: Path,
    ui_paths: tuple[Path, ...],
) -> None:
    for ui in ui_paths:
        py = (directory / ui.name).with_suffix(".py")
        qt_tool_wrapper("uic", ["-g", "python", "-o", f"{py}", f"{ui}"], True)


if __name__ == "__main__":
    main()

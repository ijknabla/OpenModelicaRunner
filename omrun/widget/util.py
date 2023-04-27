from collections.abc import Iterable

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


def make_tree(
    tree: QTreeWidget, paths: Iterable[tuple[str, ...]]
) -> dict[tuple[str, ...], QTreeWidgetItem]:
    result = dict[tuple[str, ...], QTreeWidgetItem]()
    for path in (path[:i] for path in filter(None, paths) for i, _ in enumerate(path, start=1)):
        if path in result:
            continue

        parent = result.get(path[:-1], tree)
        item = QTreeWidgetItem(parent)
        item.setText(0, path[-1])

        result[path] = item

    return result

from collections.abc import Iterable, Iterator

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


def get_tree_path(item: QTreeWidgetItem) -> tuple[str, ...]:
    return tuple(part.text(0) for part in _iter_tree_parts(item))


def _iter_tree_parts(item: QTreeWidgetItem) -> Iterator[QTreeWidgetItem]:
    parent = item.parent()
    if parent is not None:
        yield from _iter_tree_parts(parent)
    yield item

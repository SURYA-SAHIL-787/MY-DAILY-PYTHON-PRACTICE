from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
import threading


class NaryTreeError(Exception):
    pass


class InvalidNodeNameError(NaryTreeError):
    pass


class DuplicateNodeNameError(NaryTreeError):
    pass


class ParentNotFoundError(NaryTreeError):
    pass


class EmptySearchKeyError(NaryTreeError):
    pass


@dataclass
class NaryNode:
    name: str
    children: list["NaryNode"] = field(default_factory=list)

    def add_child(self, child: "NaryNode") -> None:
        self.children.append(child)


class ThreadSafeNaryTree:
    def __init__(self, root_name: str) -> None:
        self._validate_name(root_name)

        self.root = NaryNode(root_name)
        self.node_index: dict[str, NaryNode] = {
            root_name: self.root
        }

        self.lock = threading.RLock()

    def _validate_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise InvalidNodeNameError(f"Invalid node name: {name}")

    def add_child(self, parent_name: str, child_name: str) -> None:
        self._validate_name(parent_name)
        self._validate_name(child_name)

        with self.lock:
            if child_name in self.node_index:
                raise DuplicateNodeNameError(f"Duplicate node name rejected: {child_name}")

            parent = self.node_index.get(parent_name)

            if parent is None:
                raise ParentNotFoundError(f"Parent not found: {parent_name}")

            child = NaryNode(child_name)
            parent.add_child(child)
            self.node_index[child_name] = child

    def parallel_search(self, target_name: str) -> bool:
        self._validate_search_key(target_name)

        with self.lock:
            if self.root.name == target_name:
                return True

            root_children_snapshot = list(self.root.children)

        if not root_children_snapshot:
            return False

        with ThreadPoolExecutor(max_workers=len(root_children_snapshot)) as executor:
            futures = [
                executor.submit(self._dfs_search, child, target_name)
                for child in root_children_snapshot
            ]

            for future in as_completed(futures):
                if future.result():
                    return True

        return False

    def _dfs_search(self, node: NaryNode, target_name: str) -> bool:
        if node.name == target_name:
            return True

        for child in node.children:
            if self._dfs_search(child, target_name):
                return True

        return False

    def count_descendants(self, node_name: str) -> int:
        self._validate_search_key(node_name)

        with self.lock:
            node = self.node_index.get(node_name)

            if node is None:
                raise ParentNotFoundError(f"Node not found: {node_name}")

            return self._count_descendants(node)

    def _count_descendants(self, node: NaryNode) -> int:
        total = 0

        for child in node.children:
            total += 1
            total += self._count_descendants(child)

        return total

    def _validate_search_key(self, key: str) -> None:
        if not isinstance(key, str) or not key.strip():
            raise EmptySearchKeyError(f"Invalid search key: {key}")


def main() -> None:
    tree = ThreadSafeNaryTree("Company")

    operations = [
        ("Company", "Engineering"),
        ("Company", "Sales"),
        ("Company", "HR"),
        ("Engineering", "Backend"),
        ("Engineering", "Frontend"),
        ("Backend", "API"),
        ("Backend", "Database"),
        ("Frontend", "Web"),
        ("Sales", "Domestic"),
        ("Sales", "International"),
    ]

    for parent, child in operations:
        try:
            tree.add_child(parent, child)
            print(f"Added {child} under {parent}")

        except NaryTreeError as error:
            print("Add error:", error)

    invalid_operations = [
        ("Engineering", "Backend"),
        ("UnknownParent", "Legal"),
        ("HR", ""),
    ]

    for parent, child in invalid_operations:
        try:
            tree.add_child(parent, child)

        except NaryTreeError as error:
            print("Invalid add operation:", error)

    search_targets = ["API", "Finance", "International", ""]

    for target in search_targets:
        try:
            found = tree.parallel_search(target)
            print(f"Search {target}: {found}")

        except NaryTreeError as error:
            print("Search error:", error)

    count_targets = ["Company", "Engineering", "Backend", "Unknown"]

    for target in count_targets:
        try:
            count = tree.count_descendants(target)
            print(f"Descendants of {target}: {count}")

        except NaryTreeError as error:
            print("Count error:", error)


if __name__ == "__main__":
    main()

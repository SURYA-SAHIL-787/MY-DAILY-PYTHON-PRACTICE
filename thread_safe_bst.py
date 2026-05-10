from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Optional, Iterable


class TreeError(Exception):
    pass


class InvalidValueError(TreeError):
    pass


class DuplicateValueError(TreeError):
    pass


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class ThreadSafeBST:
    def __init__(self) -> None:
        self.root: Optional[Node] = None
        self.lock = threading.RLock()

    def _validate_value(self, value: int) -> None:
        if not isinstance(value, int):
            raise InvalidValueError(f"Only integers are allowed. Received: {value}")

    def insert(self, value: int) -> None:
        self._validate_value(value)

        with self.lock:
            if self.root is None:
                self.root = Node(value)
                return

            current = self.root

            while True:
                if value == current.value:
                    raise DuplicateValueError(f"Duplicate value rejected: {value}")

                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        return
                    current = current.right

    def search(self, value: int) -> bool:
        self._validate_value(value)

        with self.lock:
            current = self.root

            while current is not None:
                if value == current.value:
                    return True

                if value < current.value:
                    current = current.left
                else:
                    current = current.right

            return False

    def inorder(self) -> list[int]:
        with self.lock:
            result: list[int] = []

            def dfs(node: Optional[Node]) -> None:
                if node is None:
                    return

                dfs(node.left)
                result.append(node.value)
                dfs(node.right)

            dfs(self.root)
            return result


def insert_worker(tree: ThreadSafeBST, values: Iterable[int], worker_name: str) -> None:
    for value in values:
        try:
            tree.insert(value)
            print(f"{worker_name}: inserted {value}")
        except TreeError as error:
            print(f"{worker_name}: error -> {error}")


def search_worker(tree: ThreadSafeBST, values: Iterable[int], worker_name: str) -> None:
    for value in values:
        try:
            found = tree.search(value)
            print(f"{worker_name}: search {value} -> {found}")
        except TreeError as error:
            print(f"{worker_name}: error -> {error}")


def main() -> None:
    tree = ThreadSafeBST()

    thread_1 = threading.Thread(
        target=insert_worker,
        args=(tree, [50, 30, 70, 20], "InsertThread-1")
    )

    thread_2 = threading.Thread(
        target=insert_worker,
        args=(tree, [40, 60, 80, 30], "InsertThread-2")
    )

    thread_3 = threading.Thread(
        target=insert_worker,
        args=(tree, [10, 90, "bad-value", 100], "InsertThread-3")
    )

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()

    print("Final inorder traversal:", tree.inorder())

    search_thread = threading.Thread(
        target=search_worker,
        args=(tree, [20, 55, 80, "wrong"], "SearchThread")
    )

    search_thread.start()
    search_thread.join()


if __name__ == "__main__":
    main()

from __future__ import annotations

import threading
from collections import deque
from dataclasses import dataclass
from typing import Optional, Iterable


class BinaryTreeError(Exception):
    pass


class EmptyTreeError(BinaryTreeError):
    pass


class InvalidNodeValueError(BinaryTreeError):
    pass


class InvalidLevelOrderError(BinaryTreeError):
    pass


@dataclass
class BinaryNode:
    value: int
    left: Optional["BinaryNode"] = None
    right: Optional["BinaryNode"] = None


class BinaryTreeBuilder:
    @staticmethod
    def build_from_level_order(values: Iterable[Optional[int]]) -> BinaryNode:
        values_list = list(values)

        if not values_list:
            raise EmptyTreeError("Cannot build tree from empty input.")

        if values_list[0] is None:
            raise EmptyTreeError("Root node cannot be None.")

        for value in values_list:
            if value is not None and not isinstance(value, int):
                raise InvalidNodeValueError(f"Invalid node value: {value}")

        root = BinaryNode(values_list[0])
        queue: deque[BinaryNode] = deque([root])
        index = 1

        while queue and index < len(values_list):
            current = queue.popleft()

            if index < len(values_list):
                left_value = values_list[index]
                index += 1

                if left_value is not None:
                    current.left = BinaryNode(left_value)
                    queue.append(current.left)

            if index < len(values_list):
                right_value = values_list[index]
                index += 1

                if right_value is not None:
                    current.right = BinaryNode(right_value)
                    queue.append(current.right)

        if index < len(values_list):
            raise InvalidLevelOrderError("Unused values found in level-order input.")

        return root


class ParallelHeightCalculator:
    def __init__(self, max_thread_depth: int = 2) -> None:
        if not isinstance(max_thread_depth, int) or max_thread_depth < 0:
            raise ValueError("max_thread_depth must be a non-negative integer.")

        self.max_thread_depth = max_thread_depth

    def height(self, root: Optional[BinaryNode]) -> int:
        if root is None:
            raise EmptyTreeError("Cannot calculate height of an empty tree.")

        return self._height_parallel(root, current_depth=0)

    def _height_parallel(self, node: Optional[BinaryNode], current_depth: int) -> int:
        if node is None:
            return 0

        if current_depth >= self.max_thread_depth:
            return 1 + max(
                self._height_parallel(node.left, current_depth + 1),
                self._height_parallel(node.right, current_depth + 1)
            )

        results = {
            "left": 0,
            "right": 0,
        }

        exceptions: list[BaseException] = []

        def compute_left() -> None:
            try:
                results["left"] = self._height_parallel(node.left, current_depth + 1)
            except BaseException as error:
                exceptions.append(error)

        def compute_right() -> None:
            try:
                results["right"] = self._height_parallel(node.right, current_depth + 1)
            except BaseException as error:
                exceptions.append(error)

        left_thread = threading.Thread(target=compute_left)
        right_thread = threading.Thread(target=compute_right)

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        if exceptions:
            raise exceptions[0]

        return 1 + max(results["left"], results["right"])


def main() -> None:
    try:
        values = [10, 5, 20, 3, 7, 15, 30, 1, None, None, 8]
        root = BinaryTreeBuilder.build_from_level_order(values)

        calculator = ParallelHeightCalculator(max_thread_depth=3)
        tree_height = calculator.height(root)

        print("Tree height:", tree_height)

    except BinaryTreeError as error:
        print("Binary tree error:", error)

    except ValueError as error:
        print("Configuration error:", error)


if __name__ == "__main__":
    main()

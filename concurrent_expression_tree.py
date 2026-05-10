from __future__ import annotations

import operator
import threading
from dataclasses import dataclass
from typing import Callable, Optional


class ExpressionTreeError(Exception):
    pass


class EmptyExpressionError(ExpressionTreeError):
    pass


class InvalidTokenError(ExpressionTreeError):
    pass


class MalformedExpressionError(ExpressionTreeError):
    pass


class ExpressionDivisionByZeroError(ExpressionTreeError):
    pass


@dataclass
class ExpressionNode:
    token: str
    left: Optional["ExpressionNode"] = None
    right: Optional["ExpressionNode"] = None

    def is_operator(self) -> bool:
        return self.token in ExpressionTree.OPERATORS


class ExpressionTree:
    OPERATORS: dict[str, Callable[[float, float], float]] = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
    }

    def __init__(self, postfix_tokens: list[str]) -> None:
        self.root = self._build_tree(postfix_tokens)

    def _is_number(self, token: str) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False

    def _build_tree(self, postfix_tokens: list[str]) -> ExpressionNode:
        if not postfix_tokens:
            raise EmptyExpressionError("Postfix expression cannot be empty.")

        stack: list[ExpressionNode] = []

        for token in postfix_tokens:
            if self._is_number(token):
                stack.append(ExpressionNode(token))
            elif token in self.OPERATORS:
                if len(stack) < 2:
                    raise MalformedExpressionError(
                        f"Operator {token} does not have two operands."
                    )

                right = stack.pop()
                left = stack.pop()
                stack.append(ExpressionNode(token, left, right))
            else:
                raise InvalidTokenError(f"Invalid token found: {token}")

        if len(stack) != 1:
            raise MalformedExpressionError("Expression has unused operands or missing operators.")

        return stack[0]

    def evaluate(self, max_thread_depth: int = 2) -> float:
        if not isinstance(max_thread_depth, int) or max_thread_depth < 0:
            raise ValueError("max_thread_depth must be a non-negative integer.")

        return self._evaluate_parallel(self.root, current_depth=0, max_thread_depth=max_thread_depth)

    def _evaluate_parallel(
        self,
        node: ExpressionNode,
        current_depth: int,
        max_thread_depth: int,
    ) -> float:
        if not node.is_operator():
            return float(node.token)

        if current_depth >= max_thread_depth:
            left_value = self._evaluate_parallel(
                node.left,
                current_depth + 1,
                max_thread_depth
            )

            right_value = self._evaluate_parallel(
                node.right,
                current_depth + 1,
                max_thread_depth
            )

            return self._apply_operator(node.token, left_value, right_value)

        results = {
            "left": 0.0,
            "right": 0.0,
        }

        exceptions: list[BaseException] = []

        def evaluate_left() -> None:
            try:
                results["left"] = self._evaluate_parallel(
                    node.left,
                    current_depth + 1,
                    max_thread_depth
                )
            except BaseException as error:
                exceptions.append(error)

        def evaluate_right() -> None:
            try:
                results["right"] = self._evaluate_parallel(
                    node.right,
                    current_depth + 1,
                    max_thread_depth
                )
            except BaseException as error:
                exceptions.append(error)

        left_thread = threading.Thread(target=evaluate_left)
        right_thread = threading.Thread(target=evaluate_right)

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        if exceptions:
            raise exceptions[0]

        return self._apply_operator(node.token, results["left"], results["right"])

    def _apply_operator(self, token: str, left_value: float, right_value: float) -> float:
        if token == "/" and right_value == 0:
            raise ExpressionDivisionByZeroError("Division by zero detected.")

        return self.OPERATORS[token](left_value, right_value)


def main() -> None:
    expressions = [
        ["8", "2", "/", "3", "4", "*", "+"],
        ["10", "0", "/"],
        ["5", "6", "+", "7"],
        ["4", "x", "+"],
    ]

    for tokens in expressions:
        try:
            tree = ExpressionTree(tokens)
            result = tree.evaluate(max_thread_depth=3)
            print(tokens, "=", result)

        except ExpressionTreeError as error:
            print(tokens, "-> expression error:", error)

        except ValueError as error:
            print(tokens, "-> configuration error:", error)


if __name__ == "__main__":
    main()

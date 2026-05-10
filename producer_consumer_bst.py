from __future__ import annotations

import queue
import threading
from dataclasses import dataclass
from typing import Optional


class BSTPipelineError(Exception):
    pass


class InvalidBSTValueError(BSTPipelineError):
    pass


class DuplicateBSTValueError(BSTPipelineError):
    pass


@dataclass
class BSTNode:
    value: int
    left: Optional["BSTNode"] = None
    right: Optional["BSTNode"] = None


class ThreadSafeBST:
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None
        self.lock = threading.RLock()

    def insert(self, value: int) -> None:
        if not isinstance(value, int):
            raise InvalidBSTValueError(f"Invalid value rejected: {value}")

        with self.lock:
            if self.root is None:
                self.root = BSTNode(value)
                return

            current = self.root

            while True:
                if value == current.value:
                    raise DuplicateBSTValueError(f"Duplicate value rejected: {value}")

                if value < current.value:
                    if current.left is None:
                        current.left = BSTNode(value)
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = BSTNode(value)
                        return
                    current = current.right

    def inorder(self) -> list[int]:
        with self.lock:
            result: list[int] = []

            def dfs(node: Optional[BSTNode]) -> None:
                if node is None:
                    return

                dfs(node.left)
                result.append(node.value)
                dfs(node.right)

            dfs(self.root)
            return result


@dataclass
class WorkerStats:
    inserted: int = 0
    rejected: int = 0


class Producer:
    def __init__(self, output_queue: queue.Queue, values: list[object]) -> None:
        self.output_queue = output_queue
        self.values = values

    def produce(self) -> None:
        for value in self.values:
            self.output_queue.put(value)


class Consumer:
    SENTINEL = object()

    def __init__(
        self,
        name: str,
        input_queue: queue.Queue,
        tree: ThreadSafeBST,
        stats: WorkerStats,
    ) -> None:
        self.name = name
        self.input_queue = input_queue
        self.tree = tree
        self.stats = stats

    def consume(self) -> None:
        while True:
            value = self.input_queue.get()

            try:
                if value is self.SENTINEL:
                    return

                try:
                    self.tree.insert(value)
                    self.stats.inserted += 1
                    print(f"{self.name}: inserted {value}")

                except BSTPipelineError as error:
                    self.stats.rejected += 1
                    print(f"{self.name}: rejected {value} -> {error}")

            finally:
                self.input_queue.task_done()


class BSTProcessingPipeline:
    def __init__(self, worker_count: int) -> None:
        if not isinstance(worker_count, int) or worker_count <= 0:
            raise ValueError("worker_count must be a positive integer.")

        self.worker_count = worker_count
        self.data_queue: queue.Queue = queue.Queue()
        self.tree = ThreadSafeBST()
        self.stats = {
            f"Consumer-{index + 1}": WorkerStats()
            for index in range(worker_count)
        }

    def run(self, values: list[object]) -> None:
        producer = Producer(self.data_queue, values)

        consumers = [
            Consumer(name, self.data_queue, self.tree, stats)
            for name, stats in self.stats.items()
        ]

        consumer_threads = [
            threading.Thread(target=consumer.consume)
            for consumer in consumers
        ]

        for thread in consumer_threads:
            thread.start()

        producer_thread = threading.Thread(target=producer.produce)
        producer_thread.start()
        producer_thread.join()

        for _ in range(self.worker_count):
            self.data_queue.put(Consumer.SENTINEL)

        self.data_queue.join()

        for thread in consumer_threads:
            thread.join()

    def print_summary(self) -> None:
        print("Final BST inorder:", self.tree.inorder())

        for worker_name, stats in self.stats.items():
            print(
                worker_name,
                "inserted:",
                stats.inserted,
                "rejected:",
                stats.rejected
            )


def main() -> None:
    try:
        values = [50, 20, 70, 10, 30, 60, 80, 20, "bad", 90, 40, 70]
        pipeline = BSTProcessingPipeline(worker_count=3)
        pipeline.run(values)
        pipeline.print_summary()

    except ValueError as error:
        print("Pipeline configuration error:", error)


if __name__ == "__main__":
    main()

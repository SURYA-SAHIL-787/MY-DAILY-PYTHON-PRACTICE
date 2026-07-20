class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)

            if self.heap[index] >= self.heap[parent]:
                break

            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index]
            )
            index = parent

    def remove_min(self):
        if not self.heap:
            raise IndexError("Cannot remove from an empty heap.")

        minimum = self.heap[0]
        last_value = self.heap.pop()

        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)

        return minimum

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )
            index = smallest

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty.")

        return self.heap[0]

    def display(self):
        print("Heap:", self.heap)


def main():
    min_heap = MinHeap()

    for number in [40, 10, 30, 5, 20, 15]:
        min_heap.insert(number)

    min_heap.display()

    print("Minimum value:", min_heap.peek())
    print("Removed:", min_heap.remove_min())

    min_heap.display()


if __name__ == "__main__":
    main()

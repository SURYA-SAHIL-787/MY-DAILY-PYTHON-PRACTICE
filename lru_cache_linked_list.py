class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def _insert_at_front(self, node):
        first_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first_node
        first_node.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert_at_front(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_front(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

    def display(self):
        current = self.head.next
        result = []

        while current != self.tail:
            result.append(f"{current.key}:{current.value}")
            current = current.next

        print("Cache from most recent to least recent:", result)


def main():
    cache = LRUCache(3)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")
    cache.display()

    print("Get key 1:", cache.get(1))
    cache.display()

    cache.put(4, "D")
    cache.display()

    print("Get key 2:", cache.get(2))


if __name__ == "__main__":
    main()

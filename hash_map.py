class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
            return
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                break
            current = current.next
        current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

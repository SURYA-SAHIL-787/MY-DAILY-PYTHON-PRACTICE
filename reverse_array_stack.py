class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def display(self):
        print(self.items)


numbers = [10, 20, 30, 40, 50]

stack = Stack()

for number in numbers:
    stack.push(number)

reversed_array = []

while not stack.is_empty():
    reversed_array.append(stack.pop())

print("Original Array:", numbers)
print("Reversed Array:", reversed_array)

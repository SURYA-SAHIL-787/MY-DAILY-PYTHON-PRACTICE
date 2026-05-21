# Question:
# Take 5 numbers in a list.
# Push them into a stack.
# Pop and print them in reverse order.

numbers = [10, 20, 30, 40, 50]

stack = []

print("Original list:")
print(numbers)

for number in numbers:
    stack.append(number)
    print("Pushed into stack:", number)

print("Stack after pushing:")
print(stack)

print("Reverse order:")

while len(stack) > 0:
    removed = stack.pop()
    print("Popped from stack:", removed)

print("Stack is empty now")

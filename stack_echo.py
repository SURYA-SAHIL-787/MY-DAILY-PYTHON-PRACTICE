def stack_echo(commands):
    stack = []

    for char in commands:
        if char == "#":
            if stack:
                stack.pop()

        elif char == "!":
            if stack:
                stack.append(stack[-1])

        else:
            stack.append(char)

    return "".join(stack)


print(stack_echo("ab!#c!"))
# Output: abcc

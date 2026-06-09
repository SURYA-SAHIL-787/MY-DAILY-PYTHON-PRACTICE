def nearest_smaller_weights(weights):
    stack = []
    result = [-1] * len(weights)

    for i in range(len(weights)):
        while stack and weights[stack[-1]] >= weights[i]:
            stack.pop()

        if stack:
            result[i] = weights[stack[-1]]

        stack.append(i)

    return result


weights = [4, 5, 2, 10, 8]
print(nearest_smaller_weights(weights))

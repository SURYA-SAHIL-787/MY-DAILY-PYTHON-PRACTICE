class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_balanced_bst(numbers, start, end):
    if start > end:
        return None

    middle = (start + end) // 2

    root = Node(numbers[middle])

    root.left = create_balanced_bst(
        numbers,
        start,
        middle - 1
    )

    root.right = create_balanced_bst(
        numbers,
        middle + 1,
        end
    )

    return root


def preorder(root, result):
    if root is not None:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)


def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)


def postorder(root, result):
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)


numbers = [50, 20, 70, 10, 30, 60, 80]

numbers.sort()

root = create_balanced_bst(
    numbers,
    0,
    len(numbers) - 1
)

preorder_result = []
inorder_result = []
postorder_result = []

preorder(root, preorder_result)
inorder(root, inorder_result)
postorder(root, postorder_result)

print("Sorted Array:", numbers)
print("Preorder Traversal:", preorder_result)
print("Inorder Traversal:", inorder_result)
print("Postorder Traversal:", postorder_result)

inorder_string = " ".join(
    str(value) for value in inorder_result
)

print("Inorder as String:", inorder_string)

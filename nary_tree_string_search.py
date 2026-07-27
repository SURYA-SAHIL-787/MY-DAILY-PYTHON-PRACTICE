class NaryNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def search_tree(root, target):
    if root is None:
        return False

    if root.name.lower() == target.lower():
        return True

    for child in root.children:
        if search_tree(child, target):
            return True

    return False


root = NaryNode("College")

engineering = NaryNode("Engineering")
science = NaryNode("Science")
arts = NaryNode("Arts")

root.add_child(engineering)
root.add_child(science)
root.add_child(arts)

engineering.add_child(NaryNode("Computer Science"))
engineering.add_child(NaryNode("Mechanical"))
engineering.add_child(NaryNode("Civil"))

science.add_child(NaryNode("Physics"))
science.add_child(NaryNode("Chemistry"))

arts.add_child(NaryNode("English"))
arts.add_child(NaryNode("History"))

target = input("Enter the department to search: ")

if search_tree(root, target):
    print(target, "is present in the N-ary tree.")
else:
    print(target, "is not present in the N-ary tree.")

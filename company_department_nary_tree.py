class CompanyNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def display_structure(root, level=0):
    if root is None:
        return

    print("  " * level + root.name)

    for child in root.children:
        display_structure(child, level + 1)


def count_nodes(root):
    if root is None:
        return 0

    total = 1

    for child in root.children:
        total += count_nodes(child)

    return total


company = CompanyNode("ABC Technologies")

development = CompanyNode("Development Department")
marketing = CompanyNode("Marketing Department")
finance = CompanyNode("Finance Department")

company.add_child(development)
company.add_child(marketing)
company.add_child(finance)

development.add_child(CompanyNode("Python Developer"))
development.add_child(CompanyNode("Java Developer"))
development.add_child(CompanyNode("Web Developer"))

marketing.add_child(CompanyNode("Digital Marketer"))
marketing.add_child(CompanyNode("Content Writer"))

finance.add_child(CompanyNode("Accountant"))
finance.add_child(CompanyNode("Financial Analyst"))

print("Company organization structure:")

display_structure(company)

print("\nTotal nodes in organization:", count_nodes(company))

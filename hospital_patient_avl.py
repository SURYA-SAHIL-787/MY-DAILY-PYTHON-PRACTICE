class PatientNode:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1


class PatientAVLTree:
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0

        return (
            self.get_height(node.left)
            - self.get_height(node.right)
        )

    def right_rotate(self, node):
        new_root = node.left
        temporary = new_root.right

        new_root.right = node
        node.left = temporary

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        new_root.height = 1 + max(
            self.get_height(new_root.left),
            self.get_height(new_root.right)
        )

        return new_root

    def left_rotate(self, node):
        new_root = node.right
        temporary = new_root.left

        new_root.left = node
        node.right = temporary

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        new_root.height = 1 + max(
            self.get_height(new_root.left),
            self.get_height(new_root.right)
        )

        return new_root

    def insert(self, root, patient_id, name):
        if root is None:
            return PatientNode(patient_id, name)

        if patient_id < root.patient_id:
            root.left = self.insert(
                root.left, patient_id, name
            )
        elif patient_id > root.patient_id:
            root.right = self.insert(
                root.right, patient_id, name
            )
        else:
            return root

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # Left-Left case
        if balance > 1 and patient_id < root.left.patient_id:
            return self.right_rotate(root)

        # Right-Right case
        if balance < -1 and patient_id > root.right.patient_id:
            return self.left_rotate(root)

        # Left-Right case
        if balance > 1 and patient_id > root.left.patient_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left case
        if balance < -1 and patient_id < root.right.patient_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def display_patients(self, root):
        if root:
            self.display_patients(root.left)

            print(
                "Patient ID:",
                root.patient_id,
                "| Name:",
                root.name
            )

            self.display_patients(root.right)


tree = PatientAVLTree()
root = None

patients = [
    (104, "Aarav"),
    (102, "Meera"),
    (108, "Kiran"),
    (101, "Ananya"),
    (106, "Rahul")
]

for patient_id, name in patients:
    root = tree.insert(root, patient_id, name)

print("Patient records in ascending ID order:")

tree.display_patients(root)

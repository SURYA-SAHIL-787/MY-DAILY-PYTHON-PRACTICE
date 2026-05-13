import json
from pathlib import Path

FILE_NAME = "contacts.json"


def load_contacts():
    path = Path(FILE_NAME)

    if not path.exists():
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("\nEnter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone or not email:
        print("Name, phone, and email are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n===== CONTACT LIST =====")

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def search_contact(contacts):
    keyword = input("\nEnter name, phone, or email to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = []

    for contact in contacts:
        name = contact["name"].lower()
        phone = contact["phone"].lower()
        email = contact["email"].lower()

        if keyword in name or keyword in phone or keyword in email:
            results.append(contact)

    if not results:
        print("No matching contacts found.")
        return

    print("\nSearch Results:")

    for contact in results:
        print(f"\nName : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        deleted = contacts.pop(number - 1)
        save_contacts(contacts)
        print(f"Deleted contact: {deleted['name']}")

    except ValueError:
        print("Enter a valid number.")


def menu():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()

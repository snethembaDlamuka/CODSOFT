class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact added: {name}")

    def view_contact_list(self):
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
        print()

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details['phone']:
                results.append((name, details))
        return results

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact updated: {name}")
        else:
            print(f"Contact not found: {name}")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact deleted: {name}")
        else:
            print(f"Contact not found: {name}")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System\n")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch Results:")
                for name, details in results:
                    print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(name, phone, email, address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

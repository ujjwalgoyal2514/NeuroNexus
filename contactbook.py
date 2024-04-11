class Contact:
    def __init__(self, name, phn_num, email, address):
        self.name = name
        self.phn_num = phn_num
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phn_num}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phn_num:
                found_contacts.append(contact)
        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phn_num}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_contact_info):
        for contact in self.contacts:
            if contact.name == name:
                contact.phn_num = new_contact_info['phn_num']
                contact.email = new_contact_info['email']
                contact.address = new_contact_info['address']
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phn_num = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phn_num, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phn_num = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact_info = {'phn_num': new_phn_num, 'email': new_email, 'address': new_address}
            contact_book.update_contact(name, new_contact_info)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

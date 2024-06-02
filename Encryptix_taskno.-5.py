import tabulate

# Initialize an empty list to store contacts
contacts = []
# defining functions
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        print(tabulate.tabulate(contacts, headers="keys", tablefmt="grid"))

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            print(tabulate.tabulate([contact], headers="keys", tablefmt="grid"))
            found = True
    if not found:
        print("Contact not found!")

def update_contact():
    search_term = input("Enter name or phone number to update: ")
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            print("Update contact details:")
            contact["Name"] = input("Enter new name: ")
            contact["Phone"] = input("Enter new phone number: ")
            contact["Email"] = input("Enter new email: ")
            contact["Address"] = input("Enter new address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")
#main function to start1
def main():
    while True:
        print("------Contact Book------")
        print("\t 1. Add Contact")
        print("\t 2. View Contacts")
        print("\t 3. Search Contact")
        print("\t 4. Update Contact")
        print("\t 5. Delete Contact")
        print("\t 6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
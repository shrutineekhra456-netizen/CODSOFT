

contacts = {}

def add_contact():
    store_name = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[store_name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"✅ Contact '{store_name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for name, details in contacts.items():
        print(f"- {name} | Phone: {details['phone']}")
    print()

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details["phone"]:
            print(f"\n🔍 Found Contact:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True
    if not found:
        print("❌ Contact not found.\n")

def update_contact():
    name = input("Enter the store name to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current):")
        phone = input(f"Phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Email ({contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Address ({contacts[name]['address']}): ") or contacts[name]['address']

        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"✅ Contact '{name}' updated successfully!\n")
    else:
        print("❌ Contact not found.\n")

def delete_contact():
    name = input("Enter the store name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("❌ Contact not found.\n")

def menu():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("👋 Exiting Contact Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()

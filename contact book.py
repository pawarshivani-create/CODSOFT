#contact book
contacts = {}

def add_contact():
    name = input("Enter name of person: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved!")

def view_contacts():
    if not contacts:
        print("This contacts no not found found.")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("This contacts no not found found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Wrong choice")


contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {"Name": name, "Phone": phone}
        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        for c in contacts:
            print(c)

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        for c in contacts:
            if c["Name"].lower() == name.lower():
                print(c)
                found = True

        if not found:
            print("Contact not found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

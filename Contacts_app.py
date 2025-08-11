#importing streamlit

import streamlit as st

#Creating a new contact
contacts = {}

#Adding main menu
def show_main():
    print("Contact Manager")
    print("1. Create new contact")
    print("2. Add contact")
    print("3. Update existing contact")
    print("4. Delete a contact")
    print("5. Search contacts")
    print("6. Exit")

def create_contacts():

#Prompting user for contact details
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

    print("Contact added successfully")

#Displaying saved contacts:
    print(contacts)

#Adding a new contacts
def add_contact():
    choice = input("Do you wish to add a new contact? (Yes/No): ")
    if choice == 'Yes':
        name1 = input("Enter contact name: ")
        phone1 = input("Enter phone number: ")
        contacts[name1] = phone1
        print("Contact has been added successfully.")
    else:
        print("No contact has been added")
    print(contacts)


#Updating the contact
def update_contact():
    name_to_update = input("Enter contact name to update: ")
    new_number = input("Enter the new number: ")
    contacts[name_to_update] = new_number
    print("Contact updated successfully")
    print(contacts)

#Deleting a contact
def delete_contact():
    name_to_delete = input("Enter the contact to delete:" )
    confirm = input("Do you wish to delete the contact?(Yes/No): ")
    if confirm == 'Yes':
        del contacts[name_to_delete]
        print("Contact has been deleted.")
    else:
        print("No contact was deleted.")

#Searching for a contact
def search_contacts():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"{name} is present")
    else:
        print("contact not found")

#Creating a menu
def main():
    while True:
        show_main()
        choice = input("Choose an option (1-6): ")
        print()

        if choice == '1':
            create_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contacts()
        elif choice == '6':
            print("Goodbye")
            break
        else:
            print('Invalid choice please try again')

#Start the program
if __name__ == "__main__":
    main()



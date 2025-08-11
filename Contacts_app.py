#importing streamlit

import streamlit as st

#Creating a new contact
contacts = {}

#Adding main menu
def show_main():
    st.write("Contact Manager")
    st.write("1. Create new contact")
    st.write("2. Add contact")
    st.write("3. Update existing contact")
    st.write("4. Delete a contact")
    st.write("5. Search contacts")
    st.write("6. Exit")

def create_contacts():

#Prompting user for contact details
    name = st.text_input("Enter contact name: ")
    phone = st.number_input("Enter phone number: ")
    contacts[name] = phone

    st.write("Contact added successfully")

#Displaying saved contacts:
    st.write(contacts)

#Adding a new contacts
def add_contact():
    choice = st.text_input("Do you wish to add a new contact? (Yes/No): ")
    if choice == 'Yes':
        name1 = st.text_input("Enter contact name: ")
        phone1 = st.number_input("Enter phone number: ")
        contacts[name1] = phone1
        st.write("Contact has been added successfully.")
    else:
        st.write("No contact has been added")
    print(contacts)


#Updating the contact
def update_contact():
    name_to_update = st.text_input("Enter contact name to update: ")
    new_number = st.number_input("Enter the new number: ")
    contacts[name_to_update] = new_number
    st.write("Contact updated successfully")
    st.write(contacts)

#Deleting a contact
def delete_contact():
    name_to_delete = st.text_input("Enter the contact to delete:" )
    confirm = st.text_input("Do you wish to delete the contact?(Yes/No): ")
    if confirm == 'Yes':
        del contacts[name_to_delete]
        st.write("Contact has been deleted.")
    else:
        st.write("No contact was deleted.")

#Searching for a contact
def search_contacts():
    name = st.text_input("Enter contact name to search: ")
    if name in contacts:
        st.write(f"{name} is present")
    else:
        st.write("contact not found")

#Creating a menu
def main():
    while True:
        show_main()
        choice = st.number_input("Choose an option (1-6): ")
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
            st.write("Goodbye")
            break
        else:
            st.write('Invalid choice please try again')

#Start the program
if __name__ == "__main__":
    main()



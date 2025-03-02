# NAME= CONTACT LIST MANAGAER
'''PROJRCT FEATURES: -ADD NEW CONTACT , VIEW CONTACT , SEARCH CONTACT , DELETE CONTACT'''

'''Implimentation plan-
1.create a list to store contacts.
2. use a loop to allow users to interaact with the menu.
3.user input() to get user choices(add , view , search , delete).
4.use list operations(apped , move , iterate , search).'''

contacts = [] #list to store contacts

def add_contact():
    'function to add contacts'
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts.append({"name": name , "phone": phone , "Email": email}) #Stores contact as a dictionary


def view_contacts():
    "Function to view contacts"
    if not contacts:
        print("No contacts found. ")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts):
            print(f"{index+1}. {contact['name']} - {contact['phone']} - {contact['Email']}")
        

def search_contact():
    "function to search contacts"
    search_name = input("Search Name: ")
    for contacts in contacts:
        if contacts["name"].lower() == search_name.lower():
            print(f"found: {contacts['name']} - {contacts['phone']}")
            return
        print("Contact Not Found ! ")

def delete_contact():
    """Funcction to delete contact"""
    delete_name= input("Enter Name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print("Contact Deleted Successfully!")
            return
    print("Contact Not Found!")


#main loops
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")



options = """
1.Add Contact
2. Display contact
3. Add to File
"""
contacts, contact_index = {}, 0

def addContacts():
    global contact_index
    contact_name = input("Enter the name : ").split(",")
    phone_no = input("Enter phone number (, seprated): ").split(",")
    email = input("Enter your email: ")

    value_details = {
        "name" : contact_name,
        "Phone Nos" : phone_no,
        "email" : email
    }

    contacts[contact_index+1] = value_details
    contact_index += 1

def displayContact(id):

    name = contacts[id]["name"]
    phone = contacts[id]["Phone Nos"]
    email = contacts[id]["email"]

    print(f"Contact Name : {name}\t\tPhone Nos. : {phone}\t\tEmail : {email}")



def addToFile():

    contact_details = []
    filename = "Contact Details"
    for id,contact in contacts.items():
        contact_details.append(f"Contact Name : {contact['name']}\t\tPhone Nos. : {contact['Phone Nos']}\t\tEmail : {contact['email']}")

    with open(filename, 'w') as file:
        file.write(contact_details)



while True:

    print(f"Contact Management System: {options}")

    choice = int(input("\nEnter your choice here: "))
    if choice == 3:
        break

    match choice:
        case 1:
            addContacts()
        case 2:
            id = input("Enter the id of the contact to display: ")
            displayContact(int(id))
        case 3:
            addToFile()




from tabulate import tabulate

CHOICE_STR = """
1. Display All Contacts
2. Add Contact
3. Update Contact
4. Delete Contact
5. Exit
Enter Your Choice: """


def display_contacts(dict):
    if not dict:
        print("\nYour Contact List is empty!! \n")
        return
    headers = ['Name', 'Contact_No', 'Email_address']
    data = [[item, dict[item]['contact_no'], dict[item]['email_addr']] for item in dict]
    print(tabulate(data, headers, tablefmt='grid'))


def add_contact(contact_dict):
    name = input("\nEnter Name of new contact: ")
    if name in contact_dict:
        print("\nThe contact already exists. \n")
        return contact_dict
    contact_no = input("Enter contact number: ")
    email_addr = input("Enter email address: ")

    contact_dict[name] = {'contact_no': contact_no,
                          'email_addr': email_addr}
    return contact_dict


def update_contact(contact_dict):
    target_contact = input("Enter name of contact you want to update: ")
    if target_contact not in contact_dict:
        print(f"\ncontact of {target_contact} does not exist in your contacts! ")
        return contact_dict
    print(f"\nCurrent Contact info: \nContact_no: {contact_dict[target_contact]['contact_no']}"
          f"\nEmail_address: {contact_dict[target_contact]['email_addr']}\n")

    new_contact_no = input("New Contact_no: ")
    new_email_address = input("New Email_address: ")

    contact_dict[target_contact]['contact_no'] = new_contact_no
    contact_dict[target_contact]['email_addr'] = new_email_address

    return contact_dict

def delete_contact(contacts_dict):
    target_contact = input("Enter name of contact you want to delete: ")
    if target_contact not in contacts_dict:
        print(f"\ncontact of {target_contact} does not exist in your contacts! ")
        return contacts_dict

    del contacts_dict[target_contact]

    return contacts_dict


contacts = {}
while True:

    resp = input(CHOICE_STR)

    match resp:
        case "1":
            display_contacts(contacts)
        case "2":
            contacts = add_contact(contacts)
        case "3":
            contacts = update_contact(contacts)
        case "4":
            contacts = delete_contact(contacts)
        case "5":
            break
        case _:
            print("\nInvalid input! \n")

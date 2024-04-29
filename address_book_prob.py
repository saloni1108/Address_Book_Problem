"""
Address Book Problem
"""

import logging

logging.basicConfig(filename="address_book.log", filemode="a", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} \n Address: {self.address}, {self.city}, {self.state}, {self.zip_code} \n Phone Number: {self.phone_number} \n E-mail: {self.email}"

class AddressBook:
    def __init__(self):
        self.address_book = []

    def add_contact(self): 
        logger.info("ADDRESS BOOK STARTED...")
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        address = input("Enter the address: ")
        city = input("Enter the city of the following address: ")
        state = input("Enter the state: ")
        zip_code = input("Enter the postal code: ")
        phone_number = input("Enter a 10-digit phone number: ")
        email = input("Enter an email id: ")

        contact_1 = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        self.address_book.append(contact_1)
        logger.info("New Contact Added: %s", contact_1)

    def edit_contact(self, first_name, last_name):
        for contact in self.address_book:
            if contact.first_name ==first_name and contact.last_name == last_name:
                print("What detail would you like to edit?")
                print("1. Address \n 2. City \n 3. State \n 4. Zip Code \n 5. Phone Number \n 6. Email")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    contact.address = input("Enter new address: ")
                elif choice == 2:
                    contact.city = input("Enter new city: ")
                elif choice == 3:
                    contact.state = input("Enter new state: ")
                elif choice == 4:
                    contact.zip_code = input("Enter new zip code: ")
                elif choice == 5:
                    contact.phone_number = input("Enter new phone number: ")
                elif choice == 6:
                    contact.email = input("Enter new email: ")
                else:
                    print("Invalid choice")

                logger.info("Contact edited: %s", contact)
                return
        print("Contact not found")

    def delete_contact(self, first_name, last_name):
        for contact in self.address_book:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                logger.info("Contact deleted: %s", contact)
                print("Contact deleted successfully")
                return
        print("Contact not found")


def main():
        logger.info("Address Book Started...")
        address_book = AddressBook()

        while True:
            print("1. Add contact")
            print("2. Edit contact")
            print("3. Delete Contact")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            try:
                if choice == 1:
                    address_book.add_contact()
                    add_another = input("Do you want to input another contact into your address book (yes / no): ")
                    if add_another == 'no':
                        return main()
                    else:
                        address_book.add_contact()
                elif choice == 2:
                    first_name = input("Enter the first name of the contact: ")
                    last_name = input("Enter the last name of the contact: ")
                    address_book.edit_contact(first_name, last_name)
                elif choice ==3:
                    first_name = input("Enter the first name of the contact: ")
                    last_name = input("Enter the last name of the contact: ")
                    address_book.delete_contact(first_name, last_name)
                elif choice == 4:
                    logger.info("Address Book Closed")
                    break
                else:
                    print("Invalid choice")

            except Exception as e:
                logger.error("An Error Occurred: %s", e)       

if __name__ == "__main__":
    main()

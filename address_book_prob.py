"""
Address Book Problem
"""

import logging

# Configure logging
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


def main():
        logger.info("Address Book Started...")
        while True:
            print("1. Add contact \n 2. Exit")
            choice = int(input("Enter the choice: "))
            try:
                if choice == 1:
                    address_book = AddressBook()
                    address_book.add_contact()
                elif choice == 2:
                    logging.info("Address Book Closed")
                    break
                else:
                    raise ValueError("Wrong input entered")
            except ValueError as ve:
                logging.error("Error occurred: " + str(ve))


if __name__ == "__main__":
    main()

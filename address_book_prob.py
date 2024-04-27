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
        return "Name: {self.first_name} {self.last_name}\nAddress: {self.address}, {self.city}, {self.state}, {self.zip_code}\nPhone Number: {self.phone_number}\nE-mail: {self.email}"

def add_contact(): 
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
    logger.info("New Contact Added: ", contact_1)


def main():
    try:
        logger.info("Address Book Started...")
        add_contact()
    except Exception as e:
        logger.error("An Error Occured: %s", e)

if __name__ == "__main__":
    main()

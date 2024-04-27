"""
Address Book Problem
"""

import logging

# Configure logging
logging.basicConfig(filename="address_book.log", filemode="a", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

def add_contact(first_name, last_name, address, city, state, zip_code, phone_number, email):
    return "Name: {} {}\nAddress: {}, {}, {}, {}\nPhone Number: {}\nE-mail: {}".format(
        first_name, last_name, address, city, state, zip_code, phone_number, email)

def main():
    logger.info("ADDRESS BOOK STARTED...")
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    address = input("Enter the address: ")
    city = input("Enter the city of the following address: ")
    state = input("Enter the state: ")
    zip_code = input("Enter the postal code: ")
    phone_number = input("Enter a 10-digit phone number: ")
    email = input("Enter an email id: ")
    try:
        if all(map(str.isalpha, [first_name, last_name, city, state])) and phone_number.isdigit() and zip_code.isdigit():
            add_contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        else:
            raise Exception("Invalid Input...")
    except Exception as e:
        logger.error("An Error Occured: %s", e)

if __name__ == "__main__":
    main()

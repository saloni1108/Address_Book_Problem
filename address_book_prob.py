"""
Address Book Problem...
"""

import logging
import json
logging.basicConfig(filename="address_book.log", filemode="a", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


class Contact:
    """
    A class to represent a contact in the address book.

    Attributes:
    first_name (str): First name of the contact.
    last_name (str): Last name of the contact.
    address (str): Address of the contact.
    city (str): City of the contact.
    state (str): State of the contact.
    zip_code (str): Zip code of the contact.
    phone_number (str): Phone number of the contact.
    email (str): Email address of the contact.
    """

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        """
        Function:
        Constructs all the necessary attributes for the contact object.

        Parameters:
        first_name (str): First name of the contact.
        last_name (str): Last name of the contact.
        address (str): Address of the contact.
        city (str): City of the contact.
        state (str): State of the contact.
        zip_code (str): Zip code of the contact.
        phone_number (str): Phone number of the contact.
        email (str): Email address of the contact.

        Returns: None
        """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        """
        Returns a string representation of the contact.
        """

        return f"Name: {self.first_name} {self.last_name} \n Address: {self.address}, {self.city}, {self.state}, {self.zip_code} \n Phone Number: {self.phone_number} \n E-mail: {self.email}"
    
    def __eq__(self, other):
        """
        Function: Checks if two contact objects are equal based on their first and last names.

        Parameters:
        other (Contact): The other contact to compare with.

        Returns:
        bool: True if the contacts have the same first and last names, False otherwise.
        """
         
        return self.first_name == other.first_name and self.last_name == other.last_name

class AddressBook:
    """
    A class to represent an address book.

    Attributes:
    address_book (list): A list to store contacts.
    """

    def __init__(self):
        """
        Constructs an empty address book.
        """

        self.address_book = []

    def add_contact(self): 
        """
        Function: Adds a new contact to the address book.

        Parameter: None

        Returns: None
        """

        logger.info("ADDRESS BOOK STARTED...")
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        if any(contact.first_name == first_name and contact.last_name == last_name for contact in self.address_book):
            print("Duplicate entry! This contact already exists.")
            return
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
        """
        Function: Edits the details of an existing contact in the address book.

        Parameters:
        first_name (str): First name of the contact to edit.
        last_name (str): Last name of the contact to edit.
        
        Returns: None
        """

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
        """
        Function: Deletes a contact from the address book.

        Parameters:
        first_name (str): First name of the contact to delete.
        last_name (str): Last name of the contact to delete.

        Returns: None
        """

        for contact in self.address_book:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                logger.info("Contact deleted: %s", contact)
                print("Contact deleted successfully")
                return
        print("Contact not found")
    
    def search_by_city(self, city):
        """
        Function: Searches for contacts in a specific city.

        Parameters:
        city (str): The city to search for contacts.

        Returns:
        list: A list of contacts in the specified city.
        """

        results = []
        for contact in self.address_book:
            if contact.city == city:
                results.append(contact)
        return results
    
    def search_by_state(self, state):
        """
        Function: Searches for contacts in a specific state.

        Parameters:
        state (str): The state to search for contacts.

        Returns:
        list: A list of contacts in the specified state.
        """

        results = []
        for contact in self.address_book:
            if contact.state == state:
                results.append(contact)
        return results

    def count_by_city(self, city):
        """
        Function: Counts the number of contacts in a specific city.

        Parameters:
        city (str): The city to count contacts in.

        Returns:
        int: The number of contacts in the specified city.
        """

        count = 0
        for contact in self.address_book:
            if contact.city == city:
                count += 1
        return count
    
    def count_by_state(self, state):
        """
        Function: Counts the number of contacts in a specific state.

        Parameters:
        state (str): The state to count contacts in.

        Returns:
        int: The number of contacts in the specified state.
        """

        count = 0
        for contact in self.address_book:
            if contact.state == state:
                count+= 1
        return count

    def sort_contacts_by_name(self):
        """
        Function: Sorts the contacts in the address book by name (last name, then first name).

        Parameters: None

        Returns: None
        """

        self.address_book.sort(key=lambda contact: (contact.last_name, contact.first_name))
    
    def sort_contacts_by_city(self):
        """
        Function: Sorts the contacts in the address book by city.

        Parameters: None

        Returns: None
        """

        self.address_book.sort(key=lambda contact: contact.city)

    def sort_contacts_by_state(self):
        """
        Function: Sorts the contacts in the address book by state.
        
        Parameters: None

        Returns: None
        """

        self.address_book.sort(key=lambda contact: contact.state)

    def sort_contacts_by_zip(self):
        """
        Function: Sorts the contacts in the address book by zip code.
        
        Parameters: None

        Returns: None
        """

        self.address_book.sort(key=lambda contact: contact.zip_code)

    def read_from_json(self, filename):
        """
        Function: Reads the address book from a JSON file.

        Parameters:
        filename (str): The name of the JSON file to read from.
        
        Returns: None
        """

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for contact_info in data:
                    contact = Contact(**contact_info)
                    self.address_book.append(contact)
            print("Address book read from JSON file successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred while reading from JSON file: {e}")

    def write_to_json(self, filename):
        """
        Function: Writes the address book to a JSON file.

        Parameters:
        filename (str): The name of the JSON file to write to.
        
        Returns: None
        """

        try:
            with open(filename, 'w') as file:
                data = [contact.__dict__ for contact in self.address_book]
                json.dump(data, file, indent=4)
            print("Address book written to JSON file successfully.")
        except Exception as e:
            print(f"An error occurred while writing to JSON file: {e}")


def main():
    """
    The main function that runs the address book application.
    """
        
    logger.info("Address Book Started...")
    address_books = {}

    while True:
        print("1. Create new Address Book")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Delete Contact")
        print("5. Search a person by city or state.")
        print("6. Sort contacts by Name")
        print("7. Sort contacts by City")
        print("8. Sort contacts by State")
        print("9. Sort contacts by Zip")
        print("10. Read from a json file")
        print("11. Write to a json file")
        print("12. Exit")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                address_book_name = input("Enter the name for the new address book: ")
                address_books[address_book_name] = AddressBook()
                print(f"Address book '{address_book_name}' created successfully.")
            elif choice == 2:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    address_books[address_book_name].add_contact()
                else:
                    print("Address book not found.")
            elif choice == 3:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    first_name = input("Enter the first name of the contact: ")
                    last_name = input("Enter the last name of the contact: ")
                    new_details = {}  # Add code to get new details from the user
                    if address_books[address_book_name].edit_contact(first_name, last_name, new_details):
                        print("Contact edited successfully.")
                    else:
                        print("Contact not found.")
                else:
                    print("Address book not found.")
            elif choice == 4:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    first_name = input("Enter the first name of the contact: ")
                    last_name = input("Enter the last name of the contact: ")
                    if address_books[address_book_name].delete_contact(first_name, last_name):
                        print("Contact deleted successfully.")
                    else:
                        print("Contact not found.")
                else:
                    print("Address book not found.")
            elif choice ==5:
                city = input("Enter the city to search: ")
                state = input("Enter the state to search: ")
                found_contacts = []
                total_by_city = 0
                total_by_state = 0
                for address_book_name, address_book in address_books.items():
                    found_contacts.extend(address_book.search_by_city(city))
                    found_contacts.extend(address_book.search_by_state(state))
                    total_by_city += address_book.count_by_city(city)
                    total_by_state += address_book.count_by_state(state)
                if found_contacts:
                    print("Search results:")
                    for contact in found_contacts:
                        print(contact)
                        print(f"Total contacts in {city}: {total_by_city}")
                        print(f"Total contacts in {state}: {total_by_state}")
                else:
                    print("No contacts found in the specified city or state.")     
            elif choice == 6:
                address_book_name = input("ENter the name of the address book: ")
                if address_book_name in address_books:
                    address_books[address_book_name].sort_contacts_by_name()
                    print("Contacts sorted by name.")
                else:
                    print("Address book not found.")
            elif choice == 7:
                address_book_name = input("Enter the name of the address book: ")                    
                if address_book_name in address_books:
                    address_books[address_book_name].sort_contacts_by_city()
                    print("Contacts sorted by city.")
                else:
                    print("Address book not found.")
            elif choice == 8:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    address_books[address_book_name].sort_contacts_by_state()
                    print("Contacts sorted by state.")
                else:
                    print("Address book not found.")
            elif choice == 9:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    address_books[address_book_name].sort_contacts_by_zip()
                    print("Contacts sorted by zip code.")
                else:
                    print("Address book not found.")
            elif choice == 10:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    filename = input("Enter the filename to read from: ")
                    address_books[address_book_name].read_from_json(filename)
                else:
                    print("Address book not found.")
            elif choice == 11:
                address_book_name = input("Enter the name of the address book: ")
                if address_book_name in address_books:
                    filename = input("Enter the filename to write to: ")
                    address_books[address_book_name].write_to_json(filename)
                else:
                    print("Address book not found.")
            elif choice == 12:
                logger.info("Address Book Closed")
                break
            else:
                print("Invalid choice")

        except Exception as e:
            logger.error("An Error Occurred: %s", e)

if __name__ == "__main__":
    main()
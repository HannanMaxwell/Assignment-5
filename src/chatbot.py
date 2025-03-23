"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Muhammad Rahmani"
__version__ = "03.21.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def get_account_number() -> int:
    """Returns the account number after it validates the user input.
    
       This function checks to see if the user input is a valid account
       number and then returns the account number as an integer.

       Args:
            None.
       
       Returns:
            int: The account number.

       Raises:
            TypeError: Raised when input entered is not an integer
            ValueError: Raised when the account number entered
            does not exist in ACCOUNTS dictionary.                 
    """
    # try except catches non integer values and raises a TypeError that
    # says account number must be an int type
    try:
        # Takes the input account number from the user
        account_number = int(input("Please enter your account number: "))
    except ValueError as e:
        raise TypeError("Account number must be an int type.")
    
    # if the account number is not in ACCOUNTS dictionary, then
    # ValueError is raised saying account number does not exist
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    # returns the account_number since its valid
    return account_number

def get_amount() -> float:
    """Returns the user input as a float after asking amount to deposit.
    
       This function asks the user for the amount to deposit and then 
       returns it as a float.

       Args:
            None.
       
       Returns:
            float: The deposit amount.

       Raises:
            TypeError: Raised when input entered is not an integer
            ValueError: Raised when the amount entered is equal to
                        zero and when amount entered is less than zero.                
    """
    # try except catches non integer values and raises a ValueError that
    # says amount must be a numeric type.
    try:
        # Takes the input deposit amount from the user
        amount = float(input("Enter an amount: "))
    except ValueError as e:
        if "could not convert string to float" in str(e):
            raise TypeError("Amount must be a numeric type.")
    
    # if statement checks to see if user input entered is equal to
    # or less than 0, if it is, then raises ValueError stating to
    # the user that "Amount must be a value greater than zero."
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    # Returns the deposit amount as float
    return amount

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()

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

def get_balance(account_number: int) -> str:
    """Returns a message containing the balance of the specified account
       number.
    
       This function takes in one parameter account number as an integer
       and returns a string "Your current balance for account {account-number}
       is {balance}.

       Args:
            account_number (int): The account number.
       
       Returns:
            str: The message with account number and the balance.

       Raises:
            TypeError: Raised when account number is not an integer
            ValueError: Raised when account number does not exist
                        in the ACCOUNTS dictionary.                
    """
    # Checks to see if the account_number is an integer or not. If it is not
    # an integer, then it raises a TypeError
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    # If statement checks to see if account_number is not in ACCOUNTS 
    # dictionary, then raises a ValueError
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    balance = ACCOUNTS[account_number]["balance"]

    # returns the balance for the account number
    return f"Your current balance for account {account_number} is ${balance:,.2f}."

def make_deposit(account_number: int, amount: float) -> str:
    """Returns a string message stating the amount deposited to a specific
       account.
    
       This function takes in two parameters account_number which is an
       integer and amount which is a float and returns a message with
       the amount deposited to the account.

       Args:
            account_number (int): The account number.
            amount (float): The amount deposited.
       
       Returns:
            str: The message with amount deposited to account number.

       Raises:
            TypeError: Raised when account number is not an integer
            ValueError: Raised when account number does not exist
                        in the ACCOUNTS dictionary.
            ValueError: Raised when the amount entered is not numeric.
            ValueError: Raised when amount entered is zero or a
                        negative value.                
    """
    # if statement checks to see if account_number is an int or not
    # if it is not an int, then TypeError is raised.
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    # if statement checks to see if the account_number is in ACCOUNTS
    # dictionary. If it is not in ACCOUNTS then ValueError is raised.
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    # if the amount number is not an integer or a float, then
    # ValueError is raised.
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a numeric type.")
    # If the amount is less than or equal to zero, ValueError is raised
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    # Adds the deposit amount to the account
    ACCOUNTS[account_number]["balance"] += amount
    return f"You have made a deposit of ${amount:,.2f} to account {account_number}."

def get_task() -> str:
    """Returns a task which is a string that is entered by the user.
    
       This function prompts the user for a task. The user can enter
       balance, deposit or exit.

       Args:
            None.
       
       Returns:
            str: The task entered by the user.

       Raises:
            ValueError: Raised when the task is invalid.               
    """
    # Asks for user's input for a task
    task = input("What would you like to do (balance/deposit/exit)?: ").lower()
    # if the task is not in the VALID_TASKS, then ValueError is raised
    if task not in VALID_TASKS:
        raise ValueError(f'"{task}" is an unknown task.')
    
    return task

def chatbot():
    """Performs the Chatbot functionality.
       Presents the user with a menu of tasks to choose from such as
       balance/deposit/exit. If deposit is chosen then the amount is
       deposited into the selected account. If balance is chosen, then
       the balance of the account selected is printed. If exit is chosen
       the program exits and an exit message is printed.
    """
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")
    
    # is_valid is true until the user wants to exit the
    # loop
    is_valid = True

    # while loop keeps looping till the user wants to exit
    while is_valid:
        try:
            # gets the task from user input
            task = get_task()
            # if the task equals to exit, then the program is
            # exited
            if task == "exit":
                # Print thank you message
                print(f"Thank you for banking with {COMPANY_NAME}.")
                is_valid = False
            else:
                # Getting the account number
                account_number = get_account_number()

                # If the task is deposit, then the amount is deposited
                # and then the deposit message is displayed
                if task == "deposit":
                    amount = get_amount()
                    deposit_message = make_deposit(account_number, amount)
                    balance_message = get_balance(account_number)
                    print(deposit_message)
                    print(balance_message)
                # gets the account number and prints the account balance
                elif task == "balance":
                    balance_message = get_balance(account_number)
                    print(balance_message)
        # prints error message if it catches an error
        except Exception as e:
            print (f"Error found: {e}")

if __name__ == "__main__":
    chatbot()

"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "Muhammad Rahmani"
__version__ = "3.21.2025"

import unittest
from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS
from src.chatbot import get_account_number
from src.chatbot import get_amount
from src.chatbot import get_balance
from src.chatbot import make_deposit
from src.chatbot import get_task

class TestChatBot(unittest.TestCase):
    def test_get_account_number_non_integer(self):
        # Arrange
        # this mocks the user input as string "Hello" which is a non
        # integer
        user_input = "Hello"

        # Act
        # Mocks the input and returns "Hello"
        with patch("builtins.input", return_value=user_input):
            # Raises a TypeError by calling the get_account_number()
            # function.
            with self.assertRaises(TypeError) as context:
                get_account_number()
        
        # Assert
        expected = "Account number must be an int type."
        self.assertEqual(expected, str(context.exception))

    def test_get_account_number_does_not_exist(self):
        # Arrange
        user_input = 345678

        # Act
        # Mocks the input and returns 345678
        with patch("builtins.input", return_value=user_input):
            # Raises a ValueError by calling the get_acount_number()
            # function
            with self.assertRaises(ValueError) as context:
                get_account_number()

        # Assert
        expected = "Account number entered does not exist."
        self.assertEqual(expected, str(context.exception))

    def test_get_account_number_valid(self):
        # Arrange
        user_input = 123456

        # Act
        # Mocks the input and returns 123456
        with patch("builtins.input", return_value=user_input):
            # Calls the function get_account_number
            actual = get_account_number()
        
        # Assert
        expected = 123456
        self.assertEqual(expected, actual)

    def test_get_amount_non_integer(self):
        # Arrange
        user_input = "Not integer"

        # Act
        # Mocks the user input and returns "Not integer"
        with patch("builtins.input", return_value=user_input):
            # Raises TypeError by calling the get_amount() function
            with self.assertRaises(TypeError) as context:
                get_amount()
        
        # Assert
        expected = "Amount must be a numeric type."
        self.assertEqual(expected, str(context.exception))
    
    def test_get_amount_equals_zero(self):
        # Arrange
        user_input = 0

        # Act
        # Mocks the user input and returns 0
        with patch("builtins.input", return_value=user_input):
            # Raises ValueError by calling the get_amount()
            # function.
            with self.assertRaises(ValueError) as context:
                get_amount()
        
        # Assert
        expected = "Amount must be a value greater than zero."
        self.assertEqual(expected, str(context.exception))

    def test_get_amount_negative(self):
        # Arrange
        user_input = -1

        # Act
        # Mocks the user input and returns -1
        with patch("builtins.input", return_value=user_input):
            # Raises a ValueError by calling the get_amount()
            # function.
            with self.assertRaises(ValueError) as context:
                get_amount()
        
        # Assert
        expected = "Amount must be a value greater than zero."
        self.assertEqual(expected, str(context.exception))

    def test_get_amount_valid(self):
        # Arrange
        user_input = 330.30

        # Act
        # Mocks the user input and returns 330.30
        with patch("builtins.input", return_value=user_input):
            # Calls the function to get the actual amount
            actual = get_amount()
        
        # Assert
        expected = 330.30
        self.assertEqual(expected, actual)

    def test_get_balance_not_int(self):
        # Arrange
        invalid_account_number = "abcd"

        # Act
        # Raise TypeError by calling the function
        with self.assertRaises(TypeError) as context:
            get_balance(invalid_account_number)
        
        # Assert
        expected = "Account number must be an int type."
        self.assertEqual(expected, str(context.exception))

    def test_get_balance_does_not_exist(self):
        # Arrange
        account_number_does_not_exist = 567890

        # Act
        # Raise ValueError by calling the function
        with self.assertRaises(ValueError) as context:
            get_balance(account_number_does_not_exist)
        
        # Assert
        expected = "Account number does not exist."
        self.assertEqual(expected, str(context.exception))

    def test_get_balance_valid(self):
        # Arrange
        valid_account_number = 123456

        # Act
        actual = get_balance(valid_account_number)

        # Assert
        expected = "Your current balance for account 123456 is $1,000.00."
        self.assertEqual(expected, actual)

    def test_make_deposit_non_int_account(self):
        # Arrange
        non_int_account_number = "abcd"
        valid_amount = 500

        # Act
        with self.assertRaises(TypeError) as context:
            make_deposit(non_int_account_number, valid_amount)
        
        # Assert
        expected = "Account number must be an int type."
        self.assertEqual(expected, str(context.exception))

    def test_make_deposit_account_does_not_exist(self):
        # Arrange
        account_does_not_exist = 505050
        valid_amount = 500

        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(account_does_not_exist, valid_amount)

        # Assert
        expected = "Account number does not exist."
        self.assertEqual(expected, str(context.exception))

    def test_make_deposit_amount_zero(self):
        # Arrange
        valid_account_number = 123456
        amount_zero = 0

        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(valid_account_number, amount_zero)
        
        # Assert
        expected = "Amount must be a value greater than zero."
        self.assertEqual(expected, str(context.exception))

    def test_make_deposit_negative_amount(self):
        # Arrange
        valid_account_number = 123456
        negative_amount = -500

        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(valid_account_number, negative_amount)
        
        # Assert
        expected = "Amount must be a value greater than zero."
        self.assertEqual(expected, str(context.exception))

    def test_make_deposit_valid(self):
        # Arrange
        valid_account_number = 123456
        valid_amount = 500.50

        # Act
        actual = make_deposit(valid_account_number, valid_amount)

        # Assert
        expected = "You have made a deposit of $500.50 to account 123456."

        self.assertEqual(expected, actual)
        self.assertEqual(ACCOUNTS[123456]["balance"], 1500.50)

    def test_get_task_invalid(self):
        # Arrange
        user_input = "withdraw"

        # Act
        with patch("builtins.input", return_value=user_input):
            with self.assertRaises(ValueError) as context:
                get_task()

        # Assert
        expected = '"withdraw" is an unknown task.'
        self.assertEqual(expected, str(context.exception))

    def test_get_task_valid(self):
        # Arrange
        user_input = "balance"

        # Act
        with patch("builtins.input", return_value=user_input):
            actual = get_task()
        
        # Assert
        expected = "balance"
        self.assertEqual(expected, actual)

             
if __name__ == "__main__":
    unittest.main()
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


             

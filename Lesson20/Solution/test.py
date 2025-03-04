import unittest
from solution import add_two_numbers

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        self.assertEqual(add_two_numbers(2, 3), 5)


    def test_add_two_negative_numbers(self):
        self.assertEqual(add_two_numbers(-2, -3), 5)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add_two_numbers(2, -3), -1)

    def test_add_zero_to_number(self):
        self.assertEqual(add_two_numbers(0, -3), -3)

import unittest
from solution import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('Title', 'Author', 2000)

    def test_get_title(self):
        self.assertEqual(self.book.get_title(), 'Title')

    def test_set_title(self):
        self.book.set_title('New Title')
        self.assertEqual(self.book.get_title(), 'New Title')

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), 'Author')

    def test_set_author(self):
        self.book.set_author('New Author')
        self.assertEqual(self.book.get_author(), 'New Author')

    def test_get_year(self):
        self.assertEqual(self.book.get_year(), 2000)

    def test_set_year(self):
        self.book.set_year(2022)
        self.assertEqual(self.book.get_year(), 2022)


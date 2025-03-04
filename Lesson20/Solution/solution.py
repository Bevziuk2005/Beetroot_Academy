#task1
"""
Задайте функцію, яка повертає суму двох чисел.
Створіть тести, що перевіряють правильність роботи цієї функції для різних комбінацій чисел.
"""

def add_two_numbers(x: int, y: int) -> int:
    return x + y


#task2
"""
Створіть клас для представлення книги. 
Додайте методи для отримання/зміни інформації про книгу (назва, автор, рік видання тощо). Напишіть тести для перевірки цих методів.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

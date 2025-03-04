"""
            Task 1
"""
"""
class BankAccount:
    __account_number = 1324768
    def __init__(self, _balance):
        self._balance =  _balance

    def deposit(self, num):
        self._balance += num

    def withdraw(self, num):
        self._balance -= num

per1 = BankAccount(300)
per1.withdraw(100)
per1.deposit(50)
"""
"""
            Task 2
"""
"""
import json
class Logger:

    def __new__(self, *args, **kwargs):
        self.log.append("new")

    def __init__(self, num):
        self.num = num
        self.log = list()
        self.log.append("init")
        print(f"It's number {self.num}.")

        with open("loger.txt", "a") as file:
            json.load(self.log, file)

per = Logger(10)
"""
"""
class Logger:
    def __init__(self,filename='logs.txt'):
        self.filename = filename

    def log(self,function):
        def wrapper(*args,**kwargs):
            with open(self.filename,'w') as f:
                f.write(function.__name__)
        return wrapper



logger = Logger()

class Animal:
    def __init__(self):
        self.name = 't'
        self.age = 4
    @logger.log
    def print_hi(self):
        print('hi')

a = Animal()
a.print_hi()
"""
"""
            Task 3
"""
"""
import json
class Database:
    def __init__(self):
        self.lst = list()

    def add(self, string):
        self.lst.append(string)
        print("Add good")
        with open("database.json", "w") as file:
            json.dump(self.lst, file)

    def inf(self):
        print(self.lst)

test1 = Database()
test1.add("str")
test1.inf()
"""












































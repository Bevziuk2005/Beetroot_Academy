"""
            Task 1
"""
"""
import time
def decor(func):
    def deep():
        time.sleep(1)
        func()
    return deep

@decor
def run():
    print(993)
    while True:
        run()

run()
"""
"""
            Task 2
"""
"""
def decor(func):
    global num
    num = 0
    def deep():
        global num
        num +=1
        print (num)
        func()
    return deep

@decor
def function():
    print("Hello")

function()
function()
function()
function()
function()
"""
"""
            Task 3
"""
"""
class CubSquear():
    def __init__(self, number):
        self.number = number

    @property
    def sqrt_3(self):
        print(f"Cube Sqrt: {self.number**(1/3)}")

num1 = CubSquear(27)
num1.sqrt_3
"""
"""
            Task 4
"""
"""
class Tovard:
    def __init__(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    @property
    def cash_back(self):
        if self.age < 10:
            print(f"Cash Back: {self.age * 0.1}")
            print(f"Price: {self.price - self.price * (self.age * 0.1)}")
        else:
            print(f"Cash Back: {self.price * self.age * 0.05}")
            print(f"Price: {self.price * (self.age * 0.05)}")

t1 = Tovard("Burbon", 12, 2500)
t1.cash_back

t2 = Tovard("Vine", 3, 750)
t2.cash_back
"""
"""
            Task 5
"""
"""
class Experiments:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    @property
    def inform(self):
        print(f"{self.name}, {self.age}, {self.city}.")

    @classmethod
    def from_str(cls, string):
        name, age, city = string.split(", ")
        return cls(name, age, city)

    @classmethod
    def from_txt(cls, file_txt):
        with open(file_txt, "r") as files:
            text = files.read()
            name, age, city = text.split("\n")
        return cls(name, age, city)


test1 = Experiments("Nik", "18", "BTh")
test1.inform

test2 = Experiments.from_str("Oleg, 25, Kiev")
test2.inform

test3 = Experiments.from_txt("task22.txt")
test3.inform
"""
"""
            Task 6
"""
n = 4
m = 3

matrix =[[0, 1, 2, 3],[3, 5, 8, 3],[2, 6, 0, 9]]

for i in matrix:
    print(i)

for row in range(m):
    for col in range(n):
        if matrix[row][col] == 0:
            matrix[row] = [0 for i in range(m)]









print("\n")
for i in matrix:
    print(i)









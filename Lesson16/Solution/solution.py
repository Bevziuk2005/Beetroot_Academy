"""
           Task 1
"""
"""
class Shape:

    def __init__(self, num):
        self.num = num
    def area(self):
        print(self.num**2)

class Circl(Shape):
    def __init__(self, R):
        self.radius = R
    def area(self):
        print("Radius:", (self.radius*3.14)**2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Shape:", (self.width*self.height))

num1 = Circl(4)
num2 = Rectangle(5, 6)
num3 = Shape(3)

num1.area()
num2.area()
num3.area()
"""
"""
            Task 2
"""
"""
class Employee:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def inf(self):
        print("name: ", self.name, " money: ", self.money)

class Manager(Employee):
    def __init__(self, name, money, work):
        super().__init__(name, money)
        self.work = work

    def inf(self):
        print("name ", self.name, " money ", self.money, " work", self.work)

n1 = Employee("John", 1400)
n1.inf()
print("-------------")
n2 = Manager("Mark", 2600, 6)
n2.inf()
"""
"""
            Task 3
"""
"""
class Vector:
    def __init__(self, mn, nk, mk):
        self.mn = mn
        self.nk = nk
        self.mk = mk

    def __add__(self, a):
        print("Plus: ", self.mn+a.mn, self.nk+a.nk, self.mk+a.mk)

    def __mul__(self, scal):
        print("Multiplay: ", self.mn*scal.mn, self.nk*scal.nk, self.mk*scal.mk)

num1 = Vector(4, 5, 7)
num2 = Vector(2, 9, 1)

num1+num2
num1*num2
"""
"""
            Task 4
"""
"""
import random
class Matrix:
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
        self.matrix = [[random.randint(1, 9) for j in range(i, 8)] for i in range(8)]

    print(self.matrix)

    def __getitem__(self, item):
        print("El:", self.matrix[self.num1])

num = Matrix(1, 2)
print(num[])
"""









































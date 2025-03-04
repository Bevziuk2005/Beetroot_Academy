"""
        Task 1
"""
"""
class Book():
    def __init__(self, title, author, years, storinky):
        self.title = title
        self.author = author
        self.years = years
        self.storinky = storinky

    def inform(self):
        print(self.title, self.author, self.years, self.storinky)

book1 = Book("Karenina",  "Onegin", 1900, 2546)
book2 = Book("name23", "Dragon", 2010, 145)

book1.inform()
book2.inform()
"""
"""
        Task 2
"""
"""
class Pet():

    def __init__(self, type:str, name:str, age:int):
        self.type = type
        self.name = name
        self.age = age
        self.golos = "a"

    def inform(self):
        if self.type == "dog":
            self.golos = "Gaf"
        elif self.type == "cat":
            self.golos = "Muy"
        return self.type, self.name, self.age, self.golos
"""
"""
        Task 3
"""
"""
class Student:
    def __init__(self, name:str, age:int, city, pet):
        self.name = name
        self.age = age
        self.city = city
        self.pet = pet

    def inform(self):
        print(self.name, self.age, self.city, self.pet.inform())

pet1 = Pet("cat", "Mouse", 5)
pet2 = Pet("dog", "Tor", 2)

student1 = Student("Nikita", 18, "Bila", pet1)
student2 = Student("Oleg", 23, "London", pet2)

student1.inform()
student2.inform()
"""
"""
        Task Group 4
"""
class Order:
    def __init__(self):
        self.pizza = []
        print("New oreder (plrase input only + or -):")
        chesese = input("Chesse: ")
        if chesese == "+":
            self.pizza.append("chesse")
        meat = input("Meat: ")
        if meat == "+":
            self.pizza.append("meat")
        olives = input("Olives: ")
        if olives == "+":
            self.pizza.append("olivws")
        cucumber = input("Cucumber: ")
        if cucumber == "+":
            self.pizza.append("cucumber")
        ananas = input("Ananas: ")
        if ananas == "+":
            self.pizza.append("ananas")

    def inform(self):
        print("Your pizza:\n", self.pizza)

pizza12 = Order()
pizza12.inform()

pizz13 = Order()
pizz13.inform()


















class Authorization:
    def __init__(self):
        self.authorized = False
    def login(self, username, password):
        if username == “admin” and password == “admin”:
            self.authorized = True
            print(“Authorization successful.“)
        else:
            print(“Authorization failed.“)
    def run(self):
        username = input(“Enter username: “)
        password = input(“Enter password: “)
        self.login(username, password)


class Menu():
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def run(self):
        try:
            ek = Calculator(self.num1, self.num2)
            if self.operation == "1":
                print(ek.add())
            elif self.operation == "2":
                print(ek.sub())
            elif self.operation == "3":
                print(ek.mul())
            elif self.operation == "4":
                print(ek.div())
            elif self.operation == "5":
                print(ek.power())
        except Exception as ex:
            print(ex)

class Calculator(Menu):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return f"It's func add: {self.x + self.y}"

    def sub(self):
        return f"It's func sub: {self.x - self.y}"

    def mul(self):
        return f"It's func mul: {self.x * self.y}"

    def div(self):
        return f"{self.x % self.y}"

    def power(self):
        return f"It's func power: {self.x**self.y}"

#           TEST
authorization = Authorization()
authorization.run()
print("1. Add\n2. Subtract\n3. Multiply\n4. Divining\n5. Power")

num1 = int(input("Enter number 1: "))
num2 =  int(input("Enter number 2: "))
oper = input("Enter operation (numbers): ")

test1 = Menu(num1, num2, oper)
test1.run()

# 17.02.24

"""
number = 10


if number % 2 == 0:
    print("парне")
else:
    print("непарне")


m = 16

if m == None:
    print("none")
else:
    print(" no none")

"""

"""
n = 0

name = ""
age = ""
town = ""

while n < 3:
    if n == 0:
        name = input("name:" )
    elif n == 1:
        age = input("age:")
    else:
        town = input("town")
    n += 1


if len(name) == len(town):
    print(len(name) == len(town))
else:
    print(age)
"""

"""
for i in range(3):
   n = float(input("number1: "))
   m = float(input("number2: "))
   print(n + m)
   print(n * m)
   print(n / m)
   print(n - m)
"""

import random
"""
str = "aeyuio"
print(random.choice(str))
"""

"""
n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
print(n1, "+", n2, "=", n1 + n2)
"""

"""
n = int(input("number:" ))

while n % 2 == 0:
    m = random.randint(0, 150)
    print(n, "^", m, "=", n**m)
    break

if n % 2 != 0:
    print("welcome in the club")
"""

"""
red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

print("RGB:", red, green, blue)
"""

"""
alf = "qwertyuiopasdfghjklzxcvbnm"

for i in range(0, len(alf)):
    print(random.choice(alf))
# доробити
"""
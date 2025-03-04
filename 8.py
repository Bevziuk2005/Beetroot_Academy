"""
country = {"Ukraine": "Kiev", "Poland": "Warshava", "Spain": "Spain", "USA": "Washington"}

print(sorted(country.keys()))

print(list(reversed(sorted(country.values()))))

for key in country.keys():
    if country[key][0] == "K":
        print(key)
"""
"""
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

Discriminant = b**2 -4*a*c
print("D= ", Discriminant)

if Discriminant < 0:
    print("No corini")
elif Discriminant > 0:
    x_1 = (-b + math.sqrt(Discriminant))/ (2 * a)
    print("x_1 = ", x_1)

    x_2 = (-b - math.sqrt(Discriminant))/ (2 * a)
    print("x_2 = ", x_2)
else:
    x = -b/ (2 * a)
    print("x= ", x)
"""
"""
import random

matrix1 = [[random.randint(1, 9) for j in range(3)] for i in range(3)]
for i in matrix1:
    print(i)
print("+")
matrix2 = [[random.randint(1, 9) for j in range(3)] for i in range(3)]
for i in matrix2:
    print(i)
print("=")
matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(3)]
for i in matrix3:
    print(i)
"""
"""
def factorial(x):
    if x != 0:
        return x * factorial(x-1)
    elif x < 0:
        print("no factorial")
    else:
        return 1

print(factorial(5))
"""
"""
def fibonachi(a):

print(fibonachi(8))

# подумать для себе (2 значення. затираю поки не побачу необхідне і виводжу)
"""
"""
str1 = str(input("String: "))
def suma(str1):
    dict_alf = {}
    str2 = list(set(str1))
    for i in str2:
        dict_alf[i] = str1.count(i)
    return dict_alf

print(suma(str1))
"""
"""
list1 = list(input("Enter list: "))

def string(list_x):
    x = "".join(list_x)
    return x

print(string(list1))
"""
"""
import random

def new_matrix(a, b):
    n_matrix = [[random.randint(1, 9) for j in range(a)] for i in range(b)]
    return n_matrix
def matrix_plus(a, b):
    matrix = [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]
    return matrix

matrix_1 = new_matrix(3, 3)
matrix_2 = new_matrix(3, 3)
matrix_3 = matrix_plus(matrix_1, matrix_2)

for i in matrix_1:
    print(i)
print()
for i in matrix_2:
    print(i)
print()
for i in matrix_3:
    print(i)
"""
"""
dict1 = {}
def prosta(a, b):
    dict1[a] = b
    return dict1

print(prosta("Nikita", 18))
print(prosta("Anna", 30))
print(prosta("Oleg", 24))

print(dict1)
"""
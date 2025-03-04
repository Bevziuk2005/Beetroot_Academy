# 20.02.24

"""
list1 = {1, 2, 3, 4, 5, 6, 7, 8}
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list1.update(list2)

print(list1)
"""
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 5, 6, 9]
list1 = []
set = set(list)

for i in set:
    list1.append(i)

print(list1)
"""
"""
text = str(input("Enter a string: "))

set = set(text)
list = list(set)

for i in list:
    a = list.index(i)
    b = text.count(i)
    print(i, b)
"""
"""
import random

list_1 = []
list_2 = []
list_3 = []
n = 0

while n < 5:
    number_1 = random.randint(0, 20)
    number_2 = random.randint(0, 20)
    list_1.append(number_1)
    list_2.append(number_2)
    n += 1

print("List 1: ", list_1)
print("List 2: ", list_2)

set1 = set(list_1)
set2 = set(list_2)
set3 = set2.difference(set1)

for i in set3:
    list_3.append(i)

print("Final list: ", list_3)

for i in list_3:
    print(i**2)
"""
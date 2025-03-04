"""
dict_st = {"Nik": 18, "Mark": 25}

print(list(dict_st.values()))

dict_st["Nik"] = 20
print(dict_st)

dict_st["Oleg"] = 30

print(dict_st)

del dict_st["Mark"]
print(dict_st)
"""
"""
products = {
    "banana": 17,
    "apple": 3,
    "orange": 7,
    "pear": 19
}

print(list(products.items()))

max1 = max(products.values())
min1 = min(products.values())

sum1 = sum(products.values())
sum2 = sum1 / len(products)
print(sum2)
print(sum1)
print(max1)
print(min1)
"""
"""
import random

matrix = [(random.randint(0, 10) for i in range(5)) for j in range(5)]

for j in matrix:
    print(matrix)

for i in range(5):
    print(sum(matrix[i]))

for i in range(5):
    print(matrix[][])
"""


import random

all_list = [random.randint(1, 11) for i in range(8)]
parni_list = []
print(all_list)

for i in range(len(all_list)):
    if all_list[i] % 2 == 0:
        parni_list.append(all_list[i])
print(parni_list)

seredni = sum(parni_list) / len(parni_list)

print(seredni)

final = []

for i in range(len(parni_list)):
    if parni_list[i] > seredni:
        final.append(parni_list[i])
print(final)

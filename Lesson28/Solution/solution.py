"""
                Task 1
"""
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання функції {func.__name__}: {end - start} секунд")
        return result
    return wrapper
@timeit
def selection_sort1(list):
    sort_list = []
    a = len(list)
    for i in range(a):
        min_l = min(list)
        sort_list.append(min_l)
        list.remove(min_l)
    return sort_list
"""
list_ss = [78, 23, 8, 12, 90, 376, 56]
print(selection_sort1(list_ss))
"""
@timeit
def selection_sort2(list):
    size = len(list)
    for i in range(size):
        min = i
        for j in range(i + 1, size):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

"""
list_ss = [78, 23, 8, 12, 90, 376, 56]
print(selection_sort2(list_ss))
"""
"""
                Task 2
"""
@timeit
def insertion_sort(list):
    size = len(list)
    for i in range(1, size):
        current_value = list[i]
        pos = i
        while pos > 0 and list[pos-1] > current_value:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = current_value
    return list
"""
list_2 = [65, 8, 90, 564, 23, 14, 2, 89, 6]
print(insertion_sort(list_2))
"""
"""
            Task 3
"""
@timeit
def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

"""list_3 = [65, 8, 90, 564, 23, 14]
print(bubble_sort(list_3))
"""
"""
            Task 4
"""
import random
from timeit import timeit
import time



list_4 = [random.randint(0, 50) for _ in range(10000)]
print(len(list_4))

"""
print("select", timeit("sel", number=100, globals=globals()))
print("insert", timeit("ins", number=100, globals=globals()))
print("buble", timeit("buble", number=100, globals=globals()))
"""


selection_sort2(list_4)
insertion_sort(list_4)
bubble_sort(list_4)


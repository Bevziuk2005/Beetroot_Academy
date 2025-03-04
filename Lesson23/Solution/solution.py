# #Task 1
#
# def mult(list1: list, list2: list) -> list:
#     res = []
#     for i in range(len(list1)):
#         res.append(list1[i] * list2[i])
#     return res
#
# print(mult([1,2,3], [1,2, 3]))
#
# #O(N)
#
#
#
# #Task 2
# def print_cube(cube: list[list[list[int]]], num: int) -> int:
#     for x in range(num):
#         for y in range(num):
#             for z in range(num):
#                 print(cube[x][y][z])
#
# print_cube(
#     [
#         [
#             [1,2],
#             [3,4]
#         ],
#         [
#             [5, 6],
#             [7, 8]
#         ]
#     ], 2
# )


#Task
import timeit
import random
import time


# def sum(list: list) -> int:
#     res = 0
#     for item in list:
#         res += item
#     return res
#
#
# def mult(list: list) -> int:
#     res = 1
#     for item in list:
#         res *= item
#     return res
#
#
# l = [random.randint(1, 100) for i in range(0, 50000)]
#
#
# t1 = time.time()
# sum(l)
# t1_stop = time.time()-t1
# print("Sum time2: ", t1_stop)


# t2 = time.time()
# sum(l)
# t2_stop = time.time()-t2
# print("Mult time2: ", t2_stop)
#
# sum_time = timeit.timeit("sum(l)", number=1, globals=globals() )
# mult_time = timeit.timeit("mult(l)", number=1, globals=globals() )
#
# print("Sum time: ", sum_time)
# print("Mult time: ", mult_time)
#

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i

        while j > 0 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = x

    return arr


l = [4,2,7,5,1]
print(insertion_sort(l))



def bubble_sort_matrix(matrix):
    flat_list = sum(matrix, [])
    n = len(flat_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if flat_list[j] > flat_list[j+1]:
                flat_list[j], flat_list[j+1] = flat_list[j+1], flat_list[j]
    sorted_matrix = [flat_list[i:i+len(matrix[0])] for i in range(0, n, len(matrix[0]))]
    return sorted_matrix

matrix1 = [
    [9, 1, 3],
    [5, 2, 7],
    [6, 8, 4]
]

sorted_matrix = bubble_sort_matrix(matrix1)

for row in sorted_matrix:
    print(row)
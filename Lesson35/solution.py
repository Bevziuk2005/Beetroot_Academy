"""
            Task 1
Напишіть програму, яка використовує мультипроцесинг для генерації великої кількості випадкових чисел.
Кожен процес може генерувати числа в окремому діапазоні.
"""
"""
import multiprocessing
import random

def generator(dz):
    n1 = random.randint(1, 1000)
    n2 = random.randint(n1, 1000)
    num = [random.randint(n1, n2) for i in range(dz)]
    print(f"Diapazon({dz}): {n1}-{n2}. And num: ", num)

if __name__ == "__main__":
    random.seed(10966)
    diapazon = [random.randint(2, 10) for i in range(4)]
    print("Diapazon: ", diapazon)

    for i in range(4):
        p = multiprocessing.Process(target=generator, args=(diapazon[i], ))
        p.start()
"""
"""
            Task 2
"""
"""
import multiprocessing
import random

def part_search(searh_i, lst:list, indx):
    result = f"Its {indx+1} Proces."
    for i in lst:

        if searh_i == i:
            result = f"Its {indx+1} Proces. Search item in this."
            break
    print(result)

if __name__ == "__main__":
    random.seed(10967)
    big_list = [random.randint(1, 1000) for i in range(41)]
    print(f"Big list: {big_list}")
    s_item = 143   # search item 143
    part_len = len(big_list)//5 + len(big_list) % 5

    for i in range(part_len):
        lists = big_list[i*5:(i+1)*5]
        p = multiprocessing.Process(target=part_search, args=(s_item, lists, i, ))
        p.start()
        p.join()
"""
"""
            Task 3
"""
"""
import multiprocessing

def deep_factorial(x):
    if x == 0:
        return 1
    else:
        return x* deep_factorial(x - 1)

def work_factorial(n, num, arr):
    result = deep_factorial(n)
    arr[num.value] = result
    num.value += 1

if __name__ == "__main__":
    start_list = [1, 2, 3, 4, 5, 6, 7]
    num = multiprocessing.Value('i', 0)
    arr = multiprocessing.Array('i', len(start_list))

    for i in start_list:
        p = multiprocessing.Process(target=work_factorial, args=(i, num, arr))
        p.start()
        p.join()
    
    print("Factorials:", arr[:])
"""
"""
            Task 4
"""
import multiprocessing
import requests
def internet_inf(url_str, arr, num):
    url = url_str
    res = requests.get(url=url)
    content = res.content
    for i in content:
        arr[num.value] = i
        num.value += 1

if __name__ == "__main__":
    url_list = ["https://en.wikipedia.org/wiki/Python"]
    num = multiprocessing.Value('i', 0)
    arr = multiprocessing.Array('c', 65425)

    for url in url_list:
        p = multiprocessing.Process(target=internet_inf, args=(url, arr, num, ))
        p.start()
        p.join()

    print(arr[:].decode('utf-8'))

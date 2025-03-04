#task1
"""import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(4)
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання функції {func.__name__}: {end - start} секунд")
        return result
    return wrapper

@timeit
def fibonacci(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


fib_sequence = fibonacci(10)
print(fib_sequence)"""
from unittest import result

#task2
"""def authentication_required(user_type):
    def decorator(func):
        def wrapper(*args):

            if check_authentication():

                if user_has_access(user_type):
                    return func(*args)
                else:
                    print("You do not have sufficient permissions to access this feature.")
            else:
                print("First you need to authenticate.")

        return wrapper

    return decorator

def check_authentication():

    authenticated = True
    return authenticated

def user_has_access(user_type):
    user_type = input("User name:")
    if user_type == "admin":
        return True
    else:
        return False


@authentication_required(user_type="admin")
def admin_function():
    print("You have access to.")
admin_function()"""
#task3
"""def conversion(func):
    def wrapper():
        text = func()
        converted_text = list(text)
        print("Converted text:", converted_text)
        return converted_text
    return wrapper

@conversion
def type_text():
    text = input("Print text: ")
    return text

def end():
    print("Text conversion complete.")

text = type_text()
end()"""
#Task4
"""def handle(func):
    def wrapper(*args,):
        try:
            return func(*args,)
        except Exception as e:
            print(f"Exception '{e}' occurred while executing {func.__name__}")

    return wrapper

@handle
def example_function(y):
    x = int(input("First number(x):"))
    return x / y


result = example_function(0)

"""
"""def calculator(func):
    def wrapper(*args, **kwargs):

        try:
            result = func(*args, **kwargs)
            return result

        except ZeroDivisionError:
            print("zero division error")
        except TypeError:
            print("type error")
        except NameError:
            print("name error")
        except Exception as e:
            print("error")
    return wrapper

@calculator
def plus(x,y):

    result = x + y
    print("Result:", result)
    return result
@calculator
def minus(x,y):

    result = x - y
    print("Result:", result)
    return result
@calculator
def division(x,y):

    result = x / y
    print("Result:", result)
    return result
@calculator
def multiply(x,y):

    result = x * y
    print("Result:", result)
    return result
@calculator
def degree(x,y):

    result = x ** y
    print("Result:", result)
    return result


x = int(input("First number(x): "))
y = int(input("Second number(y): "))


def end():
    print("Corect.")



print(plus(x,y))
end()"""

"""
Симулятор гри у гонки
Перша людина пише функцію яка створює декоратори для обрахунку часу, винятків і повідомлень
Друга людина пише функцію для обрахунку характеристик 
і визначення переможця і створює набір даних машин з характеристиками

"""
import time
def total(func):
    def wrapper(times1, times2):
        try:
            start_time = time.time()
            result = func(times1, times2)
            print("Good game")
            end_time = time.time()
            final_time = (end_time - start_time) * 1000
            print(final_time)
            return result
        except Exception as e:
            print("Error", e)
    return wrapper

car = {"1": 10, "2": 15}

def distance():
    d = int(input("Print distance km: "))
    return d

def time_all(d, s):
    return d / s

d = distance()
times1 = []
times2 = []

for car_name, speed in car.items():
    t = time_all(d, speed)
    if car_name == "1":
        times1.append((car_name, t))
    elif car_name == "2":
        times2.append((car_name, t))

print("Times for each car:")
for car_name, t in times1 :
    print(f"{car_name}: {t} hours")

for car_name, t in times2 :
    print(f"{car_name}: {t} hours")
@total
def difference(times1, times2):
    for (car_name1, t1), (car_name2, t2) in zip(times1, times2):
        print(f"Difference in time between car {car_name1} and car {car_name2}: {abs(t1 - t2)} hours")
    if t1 < t2:
        print("The car 1 win")
    elif t1 > t2:
        print("The car 2 win")
    else:
        print("Not all cars were win")

difference(times1, times2)



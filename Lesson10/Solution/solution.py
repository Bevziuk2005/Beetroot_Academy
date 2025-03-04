"""
            Task 1
"""
"""
try:
    number = int(input("number: "))
    for i in range(2, number):
        if number % i == 0:
            print("no proste")
            break
        else:
            print(number)
except ValueError:
    print("float, please input integer")
except:
    print("problems")
"""

"""
            Task 2
"""
"""
try:
    string1 = input("string: ")
    fin = input("element: ")
    string2 = set(string1)
    list1 = [i for i in string2]
    if fin in list1:
        print(fin, ": ", string1.count(fin))
    else:
        raise Exception
except:
    print("problems")
"""

"""
            Task 3
"""
"""
def make_operation(arithmetic_operator, *args):
    if arithmetic_operator == '+':
        res = args[0]
        for i in args[1:]:
            res += i
    elif arithmetic_operator == '-':
        res = args[0]
        for i in args[1:]:
            res -= i
    elif arithmetic_operator == '*':
        res = args[0]
        for i in args[1:]:
            res *= i
    elif arithmetic_operator == '/':
        try:
            res = args[0]
            for i in args[1:]:
                res = res / i
        except ZeroDivisionError:
            print("no / in ziro")
    return res

try:
    number1 = int(input("number1: "))
    number2 = int(input("number2: "))
    oper = input("operation: ")
except ValueError:
    print("no numbers")
else:
    print(make_operation(oper, number1, number2))
"""

"""
            Task 5
"""
"""
dict1 = {}

while True:
    try:
        num1 = input("Number: ")
        if num1 == "stop":
            break
        num2 = int(num1)
        continue
    except Exception as ex:
        dict1[num1] = ex

print(dict1)
"""






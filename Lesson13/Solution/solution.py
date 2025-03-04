"""
            Task 1
"""
"""
import json
def cola():
    cola = input("What cola with ice (yes no): ")
    if cola == "yes":
        menu_list["Ice_in_Cola"] = "yes"
    elif cola == "no":
        menu_list["Ice_in_Cola"] = "no"

def Potato():
    potato = input("What cola with ice (s l or xl): ")
    if potato == "s":
        menu_list["Potato"] = "S"
    elif potato == "l":
        menu_list["Potato"] = "L"
    elif potato == "xl":
        menu_list["Potato"] = "XL"


while True:
    menu_list = {"Menu": "", "Ice_in_Cola": "", "Potato": ""}
    print("Menu: BigMack, CheeseBurger, Burger")
    user_menu = input("Please enter menu: ")
    if user_menu == "BigMack":
        menu_list["Menu"] = "BigMack"
        cola()
        Potato()
    elif user_menu == "CheeseBurger":
        menu_list["Menu"] = "CheeseBurger"
        cola()
        Potato()
    elif user_menu == "Burger":
        menu_list["Menu"] = "Burger"
        cola()
        Potato()
    print(f"Your menu:\n{menu_list}")
    with open("menu.json", "w") as files:
        json.dump(menu_list, files)
"""
"""
            Task 2
"""
"""
from timeit import timeit

work_list = [1, 3, 5, 7, 9] # 25

a1 = sum(work_list)
print(a1)
print(timeit(lambda: a1, number=10000))

from functools import reduce
a2 = reduce(lambda x, y: x + y, work_list)
print(a2)
print(timeit(lambda: a2, number=10000))

def func3(list):
    num = 0
    for i in list:
        num += i
    print(num)
a3 = map(func3, work_list)
print(a3)
print(timeit(lambda: a3, number=10000))
"""
"""
            Group task 3
"""
import json
with open("task.json", "r") as file:
    data = json.load(file)


print("to do, in progress, done, closed")
while True:
    task_user = input("Enter task:")
    if task_user == "create new":
        print("to do, in progress, done, closed")
        new_task = input("New task: ")
        new_status = input("New status: ")
        data.append({"name": new_task, "status": new_status})
        with open("task.json", "w") as files:
            json.dump(data, files, indent=4)
    if task_user == "delete":
        del_task = input("Delete task: ")
        for i, j in enumerate(data):
            if j["name"] == del_task:
                del data[i]
        with open("task.json", "w") as files:
            json.dump(data, files, indent=4)
    elif task_user == "stop":
        break























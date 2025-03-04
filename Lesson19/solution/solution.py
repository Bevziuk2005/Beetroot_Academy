"""
            Task 1
"""
"""
import random
def random_password():
    while True:
        i = random.randint(5, 15)
        work_password = [random.choice(j = range(0, 100)) for i in range]
        yield "".join(work_password)


gen1 = random_password()
print(next(gen1))
print(next(gen1))
"""
"""
            Task 2
"""
class Iterators:
    def __init__(self):
        with open("task_2.txt", "r") as file:
            lines = file.readlines()
        self.txt = [i for i in lines]
    def __iter__(self):
        return self
    def __next__(self):
        try:

            return "".join(self.txt[2])
        except Exception:
            return "The end"

gen2 = Iterators()
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))





















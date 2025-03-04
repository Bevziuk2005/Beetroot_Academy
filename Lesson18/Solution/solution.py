"""
            Task 1
"""
"""
class Class_1:
    def __init__(self):
        self.name = 4

    def __get__(self):
        return self.name

    def __set__(self, value):
        return self

test = Class_1
test.name = "text"
print(test.name)
"""
"""
            Task 2
"""
"""
class Class_2:
    def __init__(self):
        self._attribute = 5

    @property
    def attribute(self):
        raise Exception("Stop")


test = Class_2()
print(test.attribute)
test.attribute = 10
"""
"""
            Task 3
"""
"""
Створіть клас, що використовує дескриптор для обчислення площі прямокутника.
 Використовуйте @classmethod, щоб створити прямокутник за допомогою ширини та висоти
"""
"""
class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __get__(self):
        print(self.width * self.height)

    @classmethod
    def from_square(cls, width, height):
        print(cls(width, height))

#       TEST
test1 = Square(15, 6)
test1.from_square(test1.width, test1.height)
test1.width = test1
"""

#           Task 4

"""
Створіть клас, що використовує дескриптор для зберігання
 та обробки інформації про час у форматі годин:хвилини:секунди. 
 Використовуйте @staticmethod, щоб конвертувати час з рядка в об'єкт часу та навпаки
"""

class Time:
    def __get__(self, instance, owner):
        return f"{instance.hours}:{instance.minuts}:{instance.second}"

class Class_4:
    time = Time()
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minuts = minutes
        self.second = seconds
    @staticmethod
    def return_time(string):
        hr = string[0:2]
        min = string[3:5]
        sec = string[6:8]

        return Class_4(hr, min, sec).time
        #print(f"Test 2: {hr}, {min}, {sec}")

#       TEST
test5 = Class_4(20, 56, 90)
print(test5.return_time("56:57:20"))






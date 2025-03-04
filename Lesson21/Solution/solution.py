"""
    Task 1
"""
"""
import time
import timeit

class TimeManager:

    def __enter__(self):
        self.start = time.time()
        return self.end

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.interval = self.end - self.start
        print("The end")

with TimeManager() as tm:
    time.sleep(10)
    print(tm)
"""
"""
            Task 2
"""
"""
import re
class LoogerContextManager:
    def __init__(self, filename):
        self.filename = filename
        self.opened_file = open(self.filename)

    def log(self, message):
        print(message)

    def __enter__(self):
        return LoogerContextManager.log()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened_file.close()


with LoogerContextManager("task2.txt") as work_file:
    print(12+34)
    print(45-23)
    print(23*98)
"""
"""
            Task 3
"""
"""
import os
import shutil
class NoConstFile:

    local_directory = "D\\PyCharm Beetroote Git\\Lesson21\\Solution"
    name_directory = "Directory_task3"
    t1 = os.path.join(local_directory, name_directory)

    def __enter__(self):
        t2 = open("D\\PyCharm Beertoote Git\\Lesson21\\Solution\\Directory_task3.task3.txt", "w")
        nonlocal t2
        t2.write("Hello world")
        t2.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.move(NoConstFile.t2, )
        os.rmdir(NoConstFile.local_directory)

with NoConstFile() as files:
    print(f"test {files}")
"""
"""
            Task 4
"""
class DelText:
    global_text = ""
    del_word = []
    def __enter__(self):
        with open("text4.txt", "w+") as text_file:
            text_work = text_file.read()
            set_text = [i for i in text_work if i in set(text_work)]
            text_file.write(" ".join(str(i for i in set_text)))
            global global_text
            global_text = text_work
            global del_word
            del_word = [i for i in set_text]
        return global_text

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("text4_copy.txt", "w+") as copy_text:
            global global_text
            global del_word
            for i in del_word:
                for j in global_text:
                    if i == j:
                        global_text.replace(i, "")
            copy_text.write(global_text)

with DelText() as files:
    print(f"maybe work! {files}")


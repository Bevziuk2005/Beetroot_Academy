"""
            Task 1
"""
"""
import requests
import re

url = "https://en.wikipedia.org/wiki/Python"
res = requests.get(url=url)
content = res.text

#print(content)

f_text = re.search(r"<title>(.*?)</title>", content)

title = f_text.group(1)
print(title)
"""
"""
            Task 3
"""
"""
import requests

url = "https://en.wikipedia.org/wiki/Python"
res = requests.get(url=url)
content = res.text.split("\n")

tags = []

for char in content:
    if "<" and ">" in char:
        
        tags.append(char.replace("<", "").replace(">", ""))

f_list = []

for tag in tags:
    if "/" in tag:
        continue
    elif "\n" in tags:
        continue
    else:
        f_list.append(tag)

f_list = list(set(f_list))

for i in f_list:
    print(i)
"""
"""
            Task 2
Напишіть скрипт який буде виконувати пошук по ключовим словам за адресою: https://github.com/search?q={search_keywords}&type={search_type}"
у search_keywords потрібно передавати масив з ключовими словами по яким буде відбуватись пошук.
у search_type потрібно вказувати по чому саме потрібно вказати.
Наприклад якщо вказати search_keywords = ['python'] і search_type = 'Repositories' Тоді ми отримаємо дані про репозиторії з python які є на гітхабі.
Підказка: В результаті ви можете отримати json з якого потрібно витягнути лише назви цих репозотріїв.
"""
import requests

search_keywords = ['python']
search_type = 'repositories'

url = f"https://github.com/search?q={search_keywords}&type={search_type}"
req = requests.get(url)
rqjs = req.json()

for i in rqjs["payload"]["results"]:
    print(i["hl_name"])

# payload -> result -> hl_name

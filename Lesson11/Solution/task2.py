#task 2
"""
створити файл json з створених словників.
Створіть програму, яка зчитує дані з файлу JSON,
обчислює якусь статистику або агреговану інформацію (наприклад,
 середній вік співробітників у певному відділі) та створює звіт у форматі текстового файлу або JSON.
"""
import json

list1= [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
    ]
with open('task2.json', 'r+') as f:
    json.dump(list1, f)

def average_age(data):
    total_age = sum(person['age'] for person in data)
    return total_age / len(data)
with open('task2.json') as f:
    templates = json.load(f)
avg_age = average_age(templates)
print("Середній вік:", avg_age)
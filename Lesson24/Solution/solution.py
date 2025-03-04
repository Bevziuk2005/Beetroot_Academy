"""
        Task 1
"""
"""
class Stack:
    def __init__(self):
        self._items = []
        self.list = []

    def is_empty(self):
        return self._items == []

    def push(self, key, val):
        self._items.append({key: val})
        self.list.append(key)

    def pop(self):
        a = max(self.list)
        return self._items.pop(self._items.pop(a))

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)


s = Stack()

s.push(15, "banana")
s.push(2, "apple")

print(s.pop())
"""
"""
        Task 2
"""
"""
class Stack:
    def __init__(self):
        self._items = []

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)
        Stack.bubble_sort(self._items)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    s.push(18)
    s.push(1)
    s.push(0)
    s.push(22)
    s.push(45)
    s.push(19)
    s.push(3)

    print(s)
"""
"""
        Task 3
"""
"""
class Deque:
    def __init__(self, size):
        self._items = []
        self._size = size

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        if len(self._items)+1 > self._size:
            Deque.remove_rear()
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)
        if len(self._items) > self._size:
            Deque.remove_rear()

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"<Deque: `rear` {self._items} `front`>"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    d = Deque(5)

    d.add_front("12")
    d.add_front("20")
    d.add_front("45")
    d.add_front("10")
    d.add_front("19")
    print(d)

    d.add_front("2")
    print(d)

    d.add_rear("7")
    print(d)
"""

from itertools import compress
a = compress([1,2,3,4,5,6,7,8,9], [0, 1, 2, 3, 4, 5, 6, 7, False])
print(list(a))









"""
            Task 1
""""""
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is not None:
            if int(data) < int(self.data):
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            if int(data) > int(self.data):
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def remove(self, data, node=None):
        if self.data is not None:
            if int(data) < int(self.data):
                self.left = self.remove(data, self.left)
            elif int(data) > int(self.data):
                self.right = self.remove(data, self.right)
            else:
                if self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left
        else:
            return "Problem, no tree"

    def search(self, data):
        if int(data) < int(self.data):
            if self.left is None:
                return str(data) + " no"
            return self.left.search(data)
        else:
            if int(data) > int(self.data):
                if self.right is None:
                    return str(data) + " no"
                return self.right.search(data)
            else:
                return str(self.data) + " yes"

    def __repr__(self):
        return str(self.left) + " " + str(self.data) + " " + str(self.right)

#   TEST
bitree = BinaryTree(99)
bitree.insert(17)
bitree.insert("120")
bitree.insert("3")
bitree.insert("249")
print(bitree.remove(3))
print(bitree.search(249))

""""""
        99
    17      120
                249
                    456
                        6789
""""""
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
        self.size += 1

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right).key
            root.right = self._delete_recursive(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def where_least(self):
        least_list = []
        node = self.root
        while node is not None:
            if node.left is not None and node.right is None:
                node = node.left
            elif node.left is None and node.right is not None:
                node = node.right
            else:
                least_list.append(node.key)

        return f"In this tree {len(least_list)} least: {least_list}"

tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(14)
tree.insert(13)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)

print(tree.where_least())

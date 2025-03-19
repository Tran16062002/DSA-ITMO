import psutil
import os
from time import perf_counter
from lab2.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = TreeNode(key)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = TreeNode(key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self._min(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)
        return node

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if not node:
            return False
        if key < node.key:
            return self._exists(node.left, key)
        elif key > node.key:
            return self._exists(node.right, key)
        return True

    def next(self, key):
        result = self._next(self.root, key, None)
        return result if result is not None else "none"

    def _next(self, node, key, succ):
        if not node:
            return succ
        if node.key > key:
            return self._next(node.left, key, node.key)
        return self._next(node.right, key, succ)

    def prev(self, key):
        result = self._prev(self.root, key, None)
        return result if result is not None else "none"

    def _prev(self, node, key, pred):
        if not node:
            return pred
        if node.key < key:
            return self._prev(node.right, key, node.key)
        return self._prev(node.left, key, pred)

    def _min(self, node):
        while node.left:
            node = node.left
        return node


def process_operations(operations):
    tree = BST()
    result = []
    for operation in operations:
        op = operation.split()
        command = op[0]
        if command == "insert":
            tree.insert(int(op[1]))
        elif command == "delete":
            tree.delete(int(op[1]))
        elif command == "exists":
            result.append("true" if tree.exists(int(op[1])) else "false")
        elif command == "next":
            result.append(str(tree.next(int(op[1]))))
        elif command == "prev":
            result.append(str(tree.prev(int(op[1]))))
    return result

def task5():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    operations = read_file(PATH_INPUT)

    result = process_operations(operations)

    write_file(PATH_OUTPUT, "\n".join(result) + "\n")

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task5()

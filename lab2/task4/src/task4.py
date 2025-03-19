import random
import psutil
import os
from time import perf_counter
from lab2.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 10**9)
        self.left = None
        self.right = None
        self.size = 1

    def update_size(self):
        self.size = 1 + (self.left.size if self.left else 0) + (self.right.size if self.right else 0)

def get_size(node):
    return node.size if node else 0

def split(root, key):
    if not root:
        return None, None
    if root.key < key:
        root.right, right = split(root.right, key)
        root.update_size()
        return root, right
    else:
        left, root.left = split(root.left, key)
        root.update_size()
        return left, root

def merge(left, right):
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        left.update_size()
        return left
    else:
        right.left = merge(left, right.left)
        right.update_size()
        return right

def insert(root, key):
    if find(root, key):
        return root
    new_node = Node(key)
    left, right = split(root, key)
    return merge(merge(left, new_node), right)

def find(root, key):
    while root:
        if root.key == key:
            return True
        root = root.right if key > root.key else root.left
    return False

def kth_element(root, k):
    left_size = get_size(root.left)
    if k == left_size + 1:
        return root.key
    elif k <= left_size:
        return kth_element(root.left, k)
    else:
        return kth_element(root.right, k - left_size - 1)



def task4():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    queries = read_file(PATH_INPUT)

    results = []
    treap = None

    for query in queries:
        if not query:
            continue
        if query[0] == '+':
            x = int(query[2:])
            treap = insert(treap, x)
        elif query[0] == '?':
            k = int(query[2:])
            results.append(str(kth_element(treap, k)) + '\n')

    write_file(PATH_OUTPUT, str(''.join(results)))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task4()


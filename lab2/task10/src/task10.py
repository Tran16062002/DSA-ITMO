import psutil
import os
from time import perf_counter
from lab2.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def find_tree(data):
    tree = []
    for line in data:
        k, l, r = map(int, line.split())
        tree.append((k, l - 1 if l else -1, r - 1 if r else -1))
    return tree

def is_bst(tree, index=0, min_val=float('-inf'), max_val=float('inf')):
    if not tree or index == -1:
        return True
    key, left, right = tree[index]
    if not (min_val < key < max_val):
        return False
    return is_bst(tree, left, min_val, key) and is_bst(tree, right, key, max_val)


def task10():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n = int(data[0])
    array = data[1:]

    if n == 0:
        write_file(PATH_OUTPUT, str('YES'))
    else:
        tree = find_tree(array)
        if is_bst(tree):
            write_file(PATH_OUTPUT, str('YES'))
        else:
            write_file(PATH_OUTPUT, str('NO'))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task10()


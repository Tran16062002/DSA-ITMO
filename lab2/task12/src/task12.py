import sys
import psutil
import os
from time import perf_counter
from lab2.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

sys.setrecursionlimit(300000)


def dfs(node, tree, height, balance):
    # Если вершина пустая (ноль), высота 0
    if node == 0:
        return 0

    # Если высота для этой вершины уже вычислена, возвращаем её
    if height[node] != -1:
        return height[node]

    # Рекурсивный вызов для левого и правого поддерева
    left_height = dfs(tree[node][0], tree, height, balance)
    right_height = dfs(tree[node][1], tree, height, balance)

    # Вычисление высоты текущей вершины
    height[node] = 1 + max(left_height, right_height)

    # Баланс текущей вершины
    balance[node] = right_height - left_height

    return height[node]


def slove_data(n, data):

    if n == 0:
        return n, [], [], []

    tree = [(0, 0)] * (n + 1)
    height = [-1] * (n + 1)
    balance = [0] * (n + 1)

    for i in range(1, n+1):
        k, l, r = map(int, data[i-1].split())
        tree[i] = (l, r)

    return n, tree, height, balance


def task12():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n = int(data[0])
    data1 = data[1:]

    n, tree, height, balance = slove_data(n, data1)

    if n == 0:
        return

    dfs(1, tree, height, balance)


    write_file(PATH_OUTPUT, "\n".join(map(str, balance[1:])))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task12()

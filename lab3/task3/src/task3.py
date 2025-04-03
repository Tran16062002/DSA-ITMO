import psutil
import os
from time import perf_counter
from lab3.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def has_cycle(n, edges):
    # Состояния: 0 = не посещена, 1 = в процессе посещения, 2 = полностью обработана
    state = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    # Построение графа
    for u, v in edges:
        graph[u].append(v)

    def dfs(node):
        if state[node] == 1:  # цикл найден
            return True
        if state[node] == 2:  # уже обработана
            return False

        state[node] = 1  # помечаем как в процессе посещения
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        state[node] = 2  # помечаем как полностью обработан
        return False

    # Проверяем все вершины, так как граф может быть не связным
    for i in range(1, n + 1):
        if state[i] == 0:  # если не посещена
            if dfs(i):
                return 1  # найден цикл

    return 0

def task3():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n, m = map(int, data[0].split())
    edges = [tuple(map(int, data[i+1].split())) for i in range(m)]

    result =has_cycle(n, edges)


    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task3()



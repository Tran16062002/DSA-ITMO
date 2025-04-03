from collections import deque, defaultdict
import psutil
import os
from time import perf_counter
from lab3.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def topological_sort(n, edges):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    # Заполнение данных
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Очередь для вершин с нулевой степенью входа
    queue = deque()

    # Заполнение очереди
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    result = []
    # Основной цикл
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []


def task4():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n, m = map(int, data[0].split())
    edges = [tuple(map(int, data[i+1].split())) for i in range(m)]

    result = topological_sort(n, edges)


    write_file(PATH_OUTPUT, ' '.join(map(str, result)) + '\n')

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task4()


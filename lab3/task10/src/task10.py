import psutil
import os
from time import perf_counter
from lab3.utils import read_file, write_file
PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def bellman_ford(n, edges, s):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    reachable = [False] * (n + 1)
    reachable[s] = True

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                reachable[v] = True

    in_negative_cycle = [False] * (n + 1)
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] < INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                in_negative_cycle[v] = True
                reachable[v] = True

    for _ in range(n):
        for u, v, w in edges:
            if in_negative_cycle[u]:
                in_negative_cycle[v] = True

    result = []
    for i in range(1, n + 1):
        if not reachable[i]:
            result.append('*')
        elif in_negative_cycle[i]:
            result.append('-')
        else:
            result.append(str(dist[i]) if dist[i] != INF else '*')

    return result

def task10():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n, m = map(int, data[0].split())
    s = int(data[-1])

    edges = [tuple(map(int, data[i+1].split())) for i in range(m)]

    result = bellman_ford(n, edges, s)


    write_file(PATH_OUTPUT, "\n".join(result) + "\n")

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task10()


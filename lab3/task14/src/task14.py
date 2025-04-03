import heapq
import psutil
import os
from time import perf_counter
from lab3.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def min_time_to_reach_villages(N, d, v, R, trips):
    # Инициализируем граф
    graph = {i: [] for i in range(1, N + 1)}
    # Заполняем граф автобусными рейсами
    for start_village, start_time, end_village, end_time in trips:
        graph[start_village].append((start_time, end_village, end_time))
    # Приоритетная очередь для Dijkstra
    pq = []
    heapq.heappush(pq, (0, d))  # (время, деревня)
    # Время минимального достижения для каждой деревни
    min_time = [float('inf')] * (N + 1)
    min_time[d] = 0
    while pq:
        current_time, current_village = heapq.heappop(pq)

        # Если уже лучшее время
        if current_time > min_time[current_village]:
            continue
        # Обрабатываем все автобусные рейсы из текущей деревни
        for start_time, end_village, end_time in graph[current_village]:
            # Если мы можем сесть на автобус
            if current_time <= start_time:
                if end_time < min_time[end_village]:
                    min_time[end_village] = end_time
                    heapq.heappush(pq, (end_time, end_village))
    # Проверяем время достижения деревни v
    return min_time[v] if min_time[v] != float('inf') else -1

def task14():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    N = int(data[0].strip())
    d, v = map(int, data[1].strip().split())
    R = int(data[2].strip())
    trips = [tuple(map(int, data[i+3].strip().split())) for i in range(R)]

    result = min_time_to_reach_villages(N, d, v, R, trips)

    write_file(PATH_OUTPUT, str(result) + '\n')

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task14()

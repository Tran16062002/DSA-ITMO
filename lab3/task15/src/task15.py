from collections import deque
import psutil
import os
from time import perf_counter
from lab3.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def bfs(sx, sy, queen_pos, N, M, L, garden):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(sx, sy, 0)])
    visited = set()
    visited.add((sx, sy))

    while queue:
        x, y, time = queue.popleft()

        if (x, y) == queen_pos:
            return time

        if time < L:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (1 <= nx < N - 1) and (1 <= ny < M - 1) and (nx, ny) not in visited and garden[nx][ny] == '0':
                    visited.add((nx, ny))
                    queue.append((nx, ny, time + 1))

    return float('inf')


def task4():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    N, M = map(int, data[0].split())
    garden = [data[i+1].strip() for i in range(N)]
    Qx, Qy, L = map(int, data[N+1].strip().split())
    queen_pos = (Qx-1, Qy-1)

    total_pendants = 0

    for j in range(4):
        Ax, Ay, Pa = map(int, data[N+j+2].strip().split())
        time_to_reach = bfs(Ax-1, Ay-1, queen_pos, N, M, L, garden)
        if time_to_reach <= L:
            total_pendants += Pa

    write_file(PATH_OUTPUT, str(total_pendants) + '\n')

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task4()
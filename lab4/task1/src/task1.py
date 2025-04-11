import psutil
import os
from time import perf_counter
from lab4.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def naive_substring_search(p, t):
    positions = []
    for i in range(len(t) - len(p) + 1):
        if t[i:i + len(p)] == p:
            positions.append(i + 1)  # индексация с 1
    return positions

def task1():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    p = data[0]
    t = data[1]

    positions = naive_substring_search(p, t)

    list = []
    list.append(len(positions))
    list.append(' '.join(map(str, positions)))

    write_file(PATH_OUTPUT, '\n'''.join(map(str, list)) + '\n')

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task1()
import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def can_eat_apples(n, s, apples):

    apples_sorted = sorted(enumerate(apples, 1), key=lambda x: (min(x[1][0], x[1][1]), x[1][0]))

    order = []
    current_height = s

    for index, (a, b) in apples_sorted:
        if current_height <= a:
            return -1
        current_height -= a
        current_height += b
        order.append(index)

    return " ".join(map(str, order))

def task10():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    array = [int(i) for i in data[0].split(' ')]
    n = array[0]
    s = array[1]
    apples = []
    for i in range(1, n + 1):
        x, y = map(int, data[i].split())
        apples.append((x, y))

    result = can_eat_apples(n, s, apples)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task10()



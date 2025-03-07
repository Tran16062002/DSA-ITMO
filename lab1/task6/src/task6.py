import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


from functools import cmp_to_key

def compare(x, y):

    if x + y > y + x:
        return -1
    else:
        return 1

def largest_salary_number(numbers):

    numbers = list(map(str, numbers))

    numbers.sort(key=cmp_to_key(compare))

    return "".join(numbers) if numbers[0] != "0" else "0"

def task6():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n = int(data[0])
    numbers = [int(i) for i in data[1].split(' ')]

    result = largest_salary_number(numbers)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task6()


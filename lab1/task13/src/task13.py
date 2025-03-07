import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def can_partition(v):
    total_sum = sum(v)

    # Если сумма не делится на 3, то разделить на 3 части невозможно
    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(v)

    # Динамическое программирование для поиска возможных подмножеств
    # dp[i] будет хранить информацию, можно ли получить сумму i с помощью подмножеств
    dp = [False] * (target + 1)
    dp[0] = True  # Сумма 0 всегда достижима

    for value in v:
        for j in range(target, value - 1, -1):
            if dp[j - value]:
                dp[j] = True

    # Если сумма target достижима, то проверяем, можно ли разделить на 3 равные части
    if dp[target]:
        return 1

    return 0

def task13():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n = data[0]
    v = [int(i) for i in data[1].split(' ')]

    result = can_partition(v)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task13()


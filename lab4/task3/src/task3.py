import psutil
import os
from time import perf_counter
from lab4.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def rabin_karp(pattern, text):
    p = 31  # Простое число
    mod = 10**9 + 9  # Большое простое число для хешей

    len_p = len(pattern)
    len_t = len(text)

    # Вычисляем p^i % mod заранее
    p_pow = [1] * (max(len_p, len_t))
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i - 1] * p) % mod

    # Хеш паттерна
    hash_p = 0
    for i in range(len_p):
        hash_p = (hash_p + (ord(pattern[i]) - ord('a') + 1) * p_pow[i]) % mod

    # Префиксные хеши текста
    hash_t = [0] * (len_t + 1)
    for i in range(len_t):
        hash_t[i + 1] = (hash_t[i] + (ord(text[i]) - ord('a') + 1) * p_pow[i]) % mod

    occurrences = []
    for i in range(len_t - len_p + 1):
        # Хеш подстроки текста
        current_hash = (hash_t[i + len_p] - hash_t[i] + mod) % mod
        if current_hash == (hash_p * p_pow[i]) % mod:
            occurrences.append(i + 1)  # Переводим в нумерацию с 1

    return occurrences

def task3():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    pattern = data[0]
    text = data[1]

    result = rabin_karp(pattern, text)

    list = []
    list.append(len(result))
    list.append(' '.join(map(str, result)))

    write_file(PATH_OUTPUT, '\n'''.join(map(str, list)) + '\n')

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task3()

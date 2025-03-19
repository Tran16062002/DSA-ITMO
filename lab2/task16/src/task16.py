import bisect
import psutil
import os
from time import perf_counter
from lab2.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def process_commands(n, commands):
    """Основная функция для обработки команд."""
    elements = []
    results = []

    for command, k in commands:
        if command == +1:  # Добавить элемент
            bisect.insort(elements, k)  # Вставка с сохранением сортировки

        elif command == 0:  # Найти k-й максимум
            if 1 <= k <= len(elements):  # Проверяем, что k в допустимом диапазоне
                results.append(elements[-k])  # k-й максимум будет на индексе -k
            else:
                results.append(None)  # k-й максимум будет на индексе -k в отсортированном списке

        elif command == -1:  # Удалить элемент
            elements.remove(k)  # Удаляем элемент из списка

    return results

def task16():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n = int(data[0])
    commands = [tuple(map(int, line.split())) for line in data[1:n+1]]

    results = process_commands(n, commands)

    write_file(PATH_OUTPUT, "\n".join(map(str, results)))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task16()




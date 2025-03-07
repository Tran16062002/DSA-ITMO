import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def min_refills(d, m, stops):
    stops.append(d)  # Добавляем конечный пункт
    current_position = 0 #текущая позиция автомобиля (изначально 0)
    refills = 0  #счетчик заправок
    i = 0  # Индекс текущей заправочной станции

    while current_position < d:
        # Поиск самой дальней станции, до которой можно доехать
        last_refill = current_position
        while i < len(stops) and stops[i] - current_position <= m:
            last_refill = stops[i]
            i += 1

        # Если не удалось доехать ни до одной станции
        if last_refill == current_position:
            return -1  # Невозможно доехать

        # Обновляем текущую позицию
        current_position = last_refill
        refills += 1

    return refills - 1  # уменьшаем на 1, так как последняя остановка не считается



def task2():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    d = int(data[0])
    m = int(data[1])
    stops = [int(i) for i in data[3].split(' ')]

    result = min_refills(d, m, stops)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task2()



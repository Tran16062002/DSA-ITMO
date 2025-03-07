import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def max_expression_value(expr):
    # Преобразуем выражение в два списка: операнды и операторы
    numbers = [int(expr[i]) for i in range(0, len(expr), 2)]
    operators = [expr[i] for i in range(1, len(expr), 2)]

    n = len(numbers)

    # Массивы для хранения максимальных и минимальных значений
    max_val = [[-float('inf')] * n for _ in range(n)]
    min_val = [[float('inf')] * n for _ in range(n)]

    # Инициализация для одноэлементных подстрок
    for i in range(n):
        max_val[i][i] = numbers[i]
        min_val[i][i] = numbers[i]

    # Заполнение динамических таблиц
    for length in range(2, n + 1):  # Длина подстроки от 2 до n
        for i in range(n - length + 1):  # Начало подстроки
            j = i + length - 1  # Конец подстроки
            for k in range(i, j):  # Разделяем подстроку по операторам
                op = operators[k]  # Оператор между числами
                # Для всех возможных комбинаций применения операции
                a, b = max_val[i][k], max_val[k + 1][j]
                min_val[i][j] = min(min_val[i][j], calculate(min_val[i][k], min_val[k + 1][j], op),
                                    calculate(min_val[i][k], max_val[k + 1][j], op),
                                    calculate(max_val[i][k], min_val[k + 1][j], op),
                                    calculate(max_val[i][k], max_val[k + 1][j], op))
                max_val[i][j] = max(max_val[i][j], calculate(min_val[i][k], min_val[k + 1][j], op),
                                    calculate(min_val[i][k], max_val[k + 1][j], op),
                                    calculate(max_val[i][k], min_val[k + 1][j], op),
                                    calculate(max_val[i][k], max_val[k + 1][j], op))

    return max_val[0][n - 1]

def task14():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    expr = data[0].strip()

    result = max_expression_value(expr)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task14()


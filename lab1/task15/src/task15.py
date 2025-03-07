import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def longest_valid_bracket_sequence(s: str) -> str:
    stack = []
    valid = [False] * len(s)

    matching = {')': '(', ']': '[', '}': '{'}
    opening = {'(', '[', '{'}

    for i, char in enumerate(s):
        if char in opening:
            stack.append((char, i))
        elif char in matching:
            if stack and stack[-1][0] == matching[char]:
                _, idx = stack.pop()
                valid[i] = valid[idx] = True

    return ''.join(s[i] for i in range(len(s)) if valid[i])


def task15():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    s = data[0].strip()

    result = longest_valid_bracket_sequence(s)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task15()



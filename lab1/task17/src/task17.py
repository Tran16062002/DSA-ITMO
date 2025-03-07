import psutil
import os
from time import perf_counter
from lab1.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


MOD = 10 ** 9

# Возможные ходы коня
moves = {
    1: [6, 8], 2: [7, 9], 3: [4, 8],
    4: [3, 9, 0], 5: [], 6: [1, 7, 0],
    7: [2, 6], 8: [1, 3], 9: [2, 4],
    0: [4, 6]
}


def knight_dialer(N):
    if N == 1:
        return 8  # Все цифры, кроме 0 kniи 8

    dp = [1] * 10

    for _ in range(N - 1):
        new_dp = [0] * 10
        for digit in range(10):
            for next_digit in moves[digit]:
                new_dp[next_digit] = (new_dp[next_digit] + dp[digit]) % MOD
        dp = new_dp

    return sum(dp[d] for d in range(10) if d != 0 and d != 8) % MOD

def task17():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    N = int(data[0])

    result = knight_dialer(N)

    write_file(PATH_OUTPUT, str(result))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task17()

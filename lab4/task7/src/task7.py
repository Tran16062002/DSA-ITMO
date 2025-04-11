import psutil
import os
from time import perf_counter
from lab4.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def compute_hashes(s, length, base, mod):
    n = len(s)
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i-1] * base + ord(s[i-1])) % mod
        p[i] = (p[i-1] * base) % mod
    return h, p

def get_sub_hash(h, p, l, r, mod):
    return (h[r] - h[l] * p[r - l]) % mod

def has_common_substring(s, t, length, base1, mod1, base2, mod2):
    h1_s, p1_s = compute_hashes(s, length, base1, mod1)
    h2_s, p2_s = compute_hashes(s, length, base2, mod2)
    h1_t, p1_t = compute_hashes(t, length, base1, mod1)
    h2_t, p2_t = compute_hashes(t, length, base2, mod2)

    seen = {}
    for i in range(len(s) - length + 1):
        hs1 = get_sub_hash(h1_s, p1_s, i, i + length, mod1)
        hs2 = get_sub_hash(h2_s, p2_s, i, i + length, mod2)
        seen[(hs1, hs2)] = i

    for j in range(len(t) - length + 1):
        ht1 = get_sub_hash(h1_t, p1_t, j, j + length, mod1)
        ht2 = get_sub_hash(h2_t, p2_t, j, j + length, mod2)
        if (ht1, ht2) in seen:
            return seen[(ht1, ht2)], j
    return None

def longest_common_substring(s, t):
    base1, mod1 = 911, 10**9 + 7
    base2, mod2 = 3571, 10**9 + 9
    left, right = 0, min(len(s), len(t))
    res = (0, 0, 0)

    while left <= right:
        mid = (left + right) // 2
        found = has_common_substring(s, t, mid, base1, mod1, base2, mod2)
        if found:
            res = (found[0], found[1], mid)
            left = mid + 1
        else:
            right = mid - 1

    return res

def task7():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    results = []
    for line in data:
        s, t = line.strip().split()
        i, j, l = longest_common_substring(s, t)
        results.append(f"{i} {j} {l}")


    write_file(PATH_OUTPUT, "\n".join(results))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task7()

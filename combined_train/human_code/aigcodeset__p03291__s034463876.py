from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def f1():
    return int(input())

def f2():
    return [int(x) for v1 in input().split()]
v1 = 10 ** 9 + 7
v2 = input()
v3 = len(v2)
v4 = [0] + list(accumulate((c == 'A' for v5 in v2)))
v6 = [0] + list(accumulate((v5 == 'C' for v5 in v2)))
v7 = [0] + list(accumulate((v5 == '?' for v5 in v2)))
v8 = v7[v3]
v9 = 0
for v10 in range(1, v3 - 1):
    if v2[v10] == 'B':
        v9 += v4[v10] * (v6[v3] - v6[v10 + 1]) % v1 * pow(3, v8, v1) % v1
        if v8 >= 1:
            v9 += v7[v10] * (v6[v3] - v6[v10 + 1]) % v1 * pow(3, v8 - 1, v1) % v1
            v9 += v4[v10] * (v7[v3] - v7[v10 + 1]) % v1 * pow(3, v8 - 1, v1) % v1
        if v8 >= 2:
            v9 += v7[v10] * (v7[v3] - v7[v10 + 1]) % v1 * pow(3, v8 - 2, v1) % v1
    if v2[v10] == '?':
        v9 += v4[v10] * (v6[v3] - v6[v10 + 1]) % v1 * pow(3, v8 - 1, v1) % v1
        if v8 >= 2:
            v9 += v7[v10] * (v6[v3] - v6[v10 + 1]) % v1 * pow(3, v8 - 2, v1) % v1
            v9 += v4[v10] * (v7[v3] - v7[v10 + 1]) % v1 * pow(3, v8 - 2, v1) % v1
        if v8 >= 3:
            v9 += v7[v10] * (v7[v3] - v7[v10 + 1]) % v1 * pow(3, v8 - 3, v1) % v1
print(v9 % v1)

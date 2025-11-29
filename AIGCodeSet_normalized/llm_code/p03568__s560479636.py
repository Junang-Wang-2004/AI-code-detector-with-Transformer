from collections import deque
from functools import reduce

def f1(a1, a2):
    return a1 * a2

def f2(a1: list):
    return [True if x == 1 or x == 100 else False for v1 in a1]

def f3(a1: list):
    return [True if x % 2 == 0 else False for v1 in a1]

def f4(a1, a2: list):
    v1 = f2(a2)
    v2 = f3(a2)
    v3 = [2 if t else 3 for v4 in v1]
    v5 = [2 if o else 1 for v6 in v2]
    v7 = reduce(f1, v5)
    if sum(v1) > 0:
        v7 = v7 - 2 ** sum(v1)
    v8 = reduce(f1, v3)
    if all(v2):
        return v8 - v7
    else:
        return v8
if __name__ == '__main__':
    v1 = int(input())
    v2 = input().split(' ')
    v2 = [int(i) for v3 in v2]
    print(f4(v1, v2))

v1 = 10 ** 9 + 7
v2 = 10 ** 12
import sys
sys.setrecursionlimit(1000000)
v3 = (-1, 0, 1, 0)
v4 = (0, 1, 0, -1)
from itertools import permutations

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = {i: 0 for v4 in range(v1)}
    for v5 in v2:
        v3[v5 - 1] += 1
    for v4 in v3:
        print(v3[v4])
if __name__ == '__main__':
    f1()

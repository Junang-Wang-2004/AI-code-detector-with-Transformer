import sys
from itertools import permutations
v1 = 10 ** 9
v2 = 10 ** 9 + 7
input = lambda: sys.stdin.readline().rstrip()

def f1():
    v1, v2 = map(int, input().split())
    if v2 != 0:
        raise Exception
    v3 = [0] * 2 ** (v1 + 1)
    for v4 in range(2 ** v1):
        v3[v4] = v4
        v3[v4 + 2 ** v1] = v4
    for v4 in range(2 ** v1):
        for v5 in range(v4 + 1, 2 ** v1):
            if v3[v4] == v3[v5]:
                v3[v4] = v3[v4] ^ v3[v5]
                v3[v5] = v3[v4]
    return v3
if __name__ == '__main__':
    f1()

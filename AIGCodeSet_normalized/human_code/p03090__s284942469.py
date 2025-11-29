import sys
from itertools import product
input = sys.stdin.readline

def f1():
    v1 = int(input())
    v2 = []
    if v1 % 2 == 0:
        v3 = [(1 + i, v1 - i) for v4 in range(v1 // 2)]
    else:
        v3 = [(1 + v4, v1 - 1 - v4) for v4 in range((v1 - 1) // 2)] + [(v1,)]
    for v4 in range(len(v3) - 1):
        v5 = v3[v4]
        v6 = v3[v4 + 1]
        for v7, v8 in product(v5, v6):
            v2.append(f'{v7} {v8}')
    if len(v3) >= 3:
        v5 = v3[0]
        v6 = v3[-1]
        for v7, v8 in product(v5, v6):
            v2.append(f'{v7} {v8}')
    print(len(v2))
    print('\n'.join(v2))
if __name__ == '__main__':
    f1()

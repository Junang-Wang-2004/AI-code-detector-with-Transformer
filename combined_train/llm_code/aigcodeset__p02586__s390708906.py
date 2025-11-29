import numpy as np

def f1():
    return input()

def f2():
    return int(input())

def f3():
    return list(map(int, input().split()))

def f4(a1):
    return [int(input()) for v1 in range(a1)]

def f5(a1):
    return [input() for v1 in range(a1)]

def f6():
    v1, v2, v3 = map(int, input().split())
    v4 = [[[0] * (v2 + 1) for v5 in range(v1 + 1)] for v5 in range(4)]
    v6 = [[0] * (v2 + 1) for v5 in range(v1 + 1)]
    for v5 in range(v3):
        v7, v8, v9 = map(int, input().split())
        v6[v7][v8] = v9
    for v7 in range(1, v1 + 1):
        for v8 in range(1, v2 + 1):
            for v10 in range(0, 4):
                if v10 == 0:
                    v4[v10][v7][v8] = v4[3][v7 - 1][v8]
                else:
                    v4[v10][v7][v8] = max(v4[v10 - 1][v7][v8], v4[v10][v7][v8 - 1], v4[3][v7 - 1][v8] + v6[v7][v8], v4[v10 - 1][v7][v8 - 1] + v6[v7][v8])
    print(v4[3][v1][v2])
if __name__ == '__main__':
    f6()

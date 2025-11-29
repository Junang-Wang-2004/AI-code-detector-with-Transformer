import sys

def f1():
    v1 = 10 ** 9 + 7
    v2, v3, v4 = map(int, sys.stdin.readline().split())
    v5 = [[0] * (v3 + 1) for v6 in range(v2 + 1)]
    v5[0][0] = 1
    for v7 in range(1, v2 + 1):
        for v8 in range(v3 + 1):
            if v8 > 0:
                v5[v7][v8] = (v5[v7][v8] + v5[v7 - 1][v8 - 1]) % v1
            if v8 < v3:
                v5[v7][v8] = (v5[v7][v8] + v5[v7 - 1][v8 + 1]) % v1
            v5[v7][v8] = (v5[v7][v8] + v5[v7 - 1][v8] * (v3 - 1)) % v1
    v9 = 0
    for v8 in range(v4, v3 + 1):
        v9 = (v9 + v5[v2][v8]) % v1
    print(v9)
if __name__ == '__main__':
    f1()

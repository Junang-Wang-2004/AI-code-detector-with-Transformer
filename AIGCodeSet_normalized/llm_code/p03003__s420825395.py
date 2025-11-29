import sys

def f1():
    v1 = 10 ** 9 + 7
    v2 = lambda: [int(x) for v3 in sys.stdin.readline().split()]
    v4, v5 = v2()
    v6 = v2()
    v7 = v2()
    v8 = [[0] * (v5 + 1) for v9 in range(v4 + 1)]
    v8[0][0] = 1
    for v10 in range(1, v4 + 1):
        for v11 in range(1, v5 + 1):
            v8[v10][v11] = v8[v10 - 1][v11] + v8[v10][v11 - 1]
            if v6[v10 - 1] == v7[v11 - 1]:
                v8[v10][v11] = (v8[v10][v11] + v8[v10 - 1][v11 - 1]) % v1
    print(v8[-1][-1])
if __name__ == '__main__':
    f1()

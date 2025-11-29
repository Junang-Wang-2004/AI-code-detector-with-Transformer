import sys
v1 = sys.stdin.readline

def f1():
    v1, v2, v3 = map(int, v1().split())
    v4 = v1.bit_length()
    v5 = [[0] * v3 for v6 in range(v4)]
    v7 = [[0] * v3 for v6 in range(v4)]
    for v8 in range(v3):
        v5[0][v8] = v8 * v8 % v3
        v7[0][v8] = v8
    for v9 in range(v4 - 1):
        for v8 in range(v3):
            v5[v9 + 1][v8] = v5[v9][v5[v9][v8]]
            v7[v9 + 1][v8] = v7[v9][v8] + v7[v9][v5[v9][v8]]
    v10 = 0
    v11 = v2
    for v9 in range(v4):
        if v1 & 1 << v9:
            v10 += v7[v9][v11]
            v11 = v5[v9][v11]
    print(v10)
    return
if __name__ == '__main__':
    f1()

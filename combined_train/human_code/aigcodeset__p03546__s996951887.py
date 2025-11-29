import sys

def f1():
    input = sys.stdin.readline
    v1, v2 = map(int, input().split())
    v3 = [[int(c) for v4 in input().split()] for v5 in range(10)]
    v6 = [list(map(int, input().split())) for v5 in range(v1)]
    v7 = [[10 ** 4] * 10 for v5 in range(10)]
    for v8 in range(10):
        for v9 in range(10):
            for v10 in range(10):
                v3[v9][v10] = min(v3[v9][v10], v3[v9][v8] + v3[v8][v10])
    v11 = 0
    for v12 in v6:
        for v8 in v12:
            if v8 == -1:
                continue
            v11 += v3[v8][1]
    print(v11)
if __name__ == '__main__':
    f1()

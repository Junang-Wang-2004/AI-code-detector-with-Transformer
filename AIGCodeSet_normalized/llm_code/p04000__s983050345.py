import sys

def f1():
    v1, v2, v3 = map(int, sys.stdin.readline().split())
    v4 = [0] * 10
    v5 = (1, 0, -1, 0, 1, 1, -1, -1)
    v6 = (0, 1, 0, -1, 1, -1, 1, -1)
    v7 = {}
    for v8 in range(v3):
        v9, v10 = map(int, sys.stdin.readline().split())
        v9, v10 = (v9 - 1, v10 - 1)
        if f2(v1, v2, v9, v10):
            v7[v9, v10] = v7.get((v9, v10), 0) + 1
        for v11 in range(len(v5)):
            if f2(v1, v2, v9 + v5[v11], v10 + v6[v11]):
                v7[v9 + v5[v11], v10 + v6[v11]] = v7.get((v9 + v5[v11], v10 + v6[v11]), 0) + 1
    for v12 in v7.values():
        v4[v12] += 1
    v4[0] = (v2 - 2) * (v1 - 2) - sum(v4)
    print(*v4, sep='\n')

def f2(a1, a2, a3, a4):
    return 1 <= a3 <= a1 - 2 and 1 <= a4 <= a2 - 2
if __name__ == '__main__':
    f1()

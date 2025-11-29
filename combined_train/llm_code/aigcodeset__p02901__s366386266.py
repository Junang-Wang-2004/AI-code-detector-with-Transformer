import sys
sys.setrecursionlimit(10 ** 9)
v1 = 10 ** 20

def f1():
    v1, v2 = map(int, input().split())
    v3 = []
    v4 = [[v1] * 2 for v5 in range(v1 + 1)]
    for v6 in range(v2):
        v7, v5 = map(int, input().split())
        v8 = set(map(int, input().split()))
        v3.append((v7, v8))
        for v9 in range(1, v1 + 1):
            if v9 in v8:
                if v4[v9][0] > v7:
                    v4[v9][0] = v7
                    v4[v9][1] = v6
    v10 = v1
    for v6 in range(2 ** (v1 + 1)):
        v11 = 0
        v12 = set()
        for v9 in range(1, v1 + 1):
            if v6 >> v9 & 1:
                if v4[v9][0] == v1:
                    print(-1)
                    exit()
                v11 += v4[v9][0]
                v12 = v12.union(v3[v4[v9][1]][1])
        if len(v12) == v1:
            v10 = min(v10, v11)
    print(v10 if v10 != v1 else -1)
if __name__ == '__main__':
    f1()

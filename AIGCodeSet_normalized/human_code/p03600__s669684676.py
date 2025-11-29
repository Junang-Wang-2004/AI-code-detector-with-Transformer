import sys
v1 = sys.stdin.read
v2 = sys.stdin.readline
v3 = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
v4 = 1 << 60

def f1():
    v1 = int(v2())
    v2 = [list(map(int, v2().split())) for v3 in range(v1)]
    v4 = [[True] * v1 for v3 in range(v1)]
    for v5 in range(v1):
        for v6 in range(v1):
            for v7 in range(v6 + 1, v1):
                if v2[v6][v7] > v2[v6][v5] + v2[v5][v7]:
                    print(-1)
                    return
                if v5 not in (v6, v7) and v2[v6][v7] == v2[v6][v5] + v2[v5][v7]:
                    v4[v6][v7] = False
    v8 = 0
    for v6 in range(v1):
        for v7 in range(v6 + 1, v1):
            if v4[v6][v7]:
                v8 += v2[v6][v7]
    print(v8)
    return
if __name__ == '__main__':
    f1()

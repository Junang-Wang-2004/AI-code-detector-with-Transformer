import sys

def f1(a1, a2):
    v1 = [0] * a1
    v2 = [[-1] * a1 for v3 in range(a1)]
    for v4 in range(a1):
        v2[v4][0] = 0
    while True:
        v5 = True
        for v6 in range(a1):
            if v1[v6] >= a1 - 1:
                continue
            v7 = a2[v6][v1[v6]]
            if a2[v7][v1[v7]] == v6:
                v8 = max(v2[v6][v1[v6]], v2[v7][v1[v7]])
                v1[v6] += 1
                v1[v7] += 1
                v2[v6][v1[v6]] = v8 + 1
                v2[v7][v1[v7]] = v8 + 1
                v5 = False
        if v5:
            break
    v9 = -1
    for v6 in range(a1):
        v9 = max(v9, v2[v6][a1 - 1])
    print(v9)
if __name__ == '__main__':
    input = sys.stdin.readline
    v1 = int(input())
    v2 = [list(map(lambda x: int(x) - 1, input().split())) for v3 in range(v1)]
    f1(v1, v2)

def f1():
    v1 = int(input())
    v2 = [list(map(int, input().split())) for v3 in range(v1)]
    v4 = 0
    for v5 in range(v1):
        v2[v5][v5] = float('INF')
    for v5 in range(v1):
        for v6 in range(v5):
            if v5 == v6:
                v2[v5][v6] = float('INF')
                continue
            v7 = min(map(sum, zip(v2[v5], v2[v6])))
            if v2[v5][v6] > v7:
                print(-1)
                return
            if v7 > v2[v5][v6]:
                v4 += v2[v5][v6]
    print(v4)
f1()

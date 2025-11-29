def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    while True:
        for v3 in range(1, len(v2)):
            v2[v3] = v2[v3] % v2[0]
        if 0 in v2:
            v2 = list(set(v2))
            v2.remove(0)
        if len(v2) == 2:
            if v2[1] < v2[0]:
                v2[0] -= v2[1]
                continue
            v4 = v2[1] - v2[0]
            v2[0] = v4
            v2.remove(v2[1])
        if len(v2) == 1:
            break
    print(v2[0])
f1()

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = v1
    v4 = 0
    v5 = v2[0]
    for v6 in range(1, v1):
        if v5 & v2[v6] == 0:
            v5 = v5 ^ v2[v6]
            continue
        v5 = v5 ^ v2[v6]
        v7 = v6 - 1
        while v7 >= v4:
            if v2[v7] & v2[v6] != 0:
                break
            v7 -= 1
        v7 += 1
        for v8 in range(v4, v7):
            v5 = v5 ^ v2[v8]
        v3 += (v6 - v4) * (v6 - v4 - 1) // 2 - (v6 - v7) * (v6 - v7 - 1) // 2
        v4 = v7
    v6 += 1
    v3 += (v6 - v4) * (v6 - v4 - 1) // 2
    print(v3)
f1()

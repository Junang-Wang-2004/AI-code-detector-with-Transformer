def f1():
    return list(map(int, input().split()))
v1 = int(input())
v2 = f1()
v2 = sorted(v2)
if v2[0] >= 0:
    v3 = sum(v2) - 2 * v2[0]
    print(v3)
    v4 = v2[0]
    for v5 in range(v1 - 2):
        v6 = v2[v5 + 1]
        print(v4, v6)
        v4 -= v6
    print(v2[-1], v4)
elif v2[-1] <= 0:
    v3 = -sum(v2) + 2 * v2[-1]
    print(v3)
    v4 = v2[-1]
    for v5 in range(v1 - 2):
        v6 = v2[-2 - v5]
        print(v4, v6)
        v4 -= v6
    print(v4, v2[0])
else:
    v3 = 0
    for v5 in range(v1):
        v3 += abs(v2[v5])
    print(v3)
    for v5 in range(v1):
        if v2[v5] > 0:
            v7 = v5
            break
    v8 = []
    v9 = []
    for v5 in range(v1):
        if v2[v5] < 0:
            v8.append(v2[v5])
        else:
            v9.append(v2[v5])
    v10 = len(v8)
    v11 = len(v9)
    v4 = v8[0]
    for v5 in range(v11 - 1):
        v6 = v9[v5]
        print(v4, v6)
        v4 -= v6
    v8[0] = v4
    v4 = v9[-1]
    for v5 in range(v10):
        v6 = v8[v5]
        print(v4, v6)
        v4 -= v6

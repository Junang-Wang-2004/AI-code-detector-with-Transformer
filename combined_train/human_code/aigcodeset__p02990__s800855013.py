v1, v2 = map(int, input().split())
v3 = [1] * (v1 + 2)
for v4 in range(1, v1 + 2):
    v3[v4] = v3[v4 - 1] * v4
v5 = 10 ** 9 + 7

def f1(a1, a2):
    if a1 < 0 or a2 < 0:
        return 1
    return v3[a1] // v3[a1 - a2] // v3[a2]
for v4 in range(1, v2 + 1):
    if v1 - v2 + 1 < v4:
        print(0)
        continue
    v6 = f1(v2 - 1, v4 - 1)
    v7 = 0
    if v4 == 1:
        v7 = v1 - v2 + 1
    elif v4 + 1 <= v1 - v2:
        v7 += f1(v1 - v2 - 1, v4 - 2)
        v7 += 2 * f1(v1 - v2 - 1, v4 - 1)
        v7 += f1(v1 - v2 - 1, v4)
    elif v4 == v1 - v2:
        v7 += f1(v1 - v2 - 1, v4 - 2)
        v7 += 2 * f1(v1 - v2 - 1, v4 - 1)
    elif v4 - 1 == v1 - v2:
        v7 += f1(v1 - v2 - 1, v4 - 2)
    else:
        v7 += 0
    print(v6 * v7 % v5)

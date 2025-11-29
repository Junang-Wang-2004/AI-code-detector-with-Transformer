v1 = 998244353
v2, v3, v4 = map(int, input().split())
v5 = [0] + [1]
for v6 in range(2, v4 + 2):
    v5.append(-(v1 // v6) * v5[v1 % v6] % v1)

def f1(a1, a2):
    if a2 == 0:
        return 1
    else:
        v1 = f1(a1, a2 // 2)
        if a2 % 2 == 0:
            return v1 ** 2 % v1
        else:
            return a1 * v1 ** 2 % v1

def f2(a1):
    return f1(a1, v1 - 2)
if v3 == 1 and v4 < v2 - 1:
    print(0)
elif v4 == v2 - 1:
    print(f1(v3, v2))
else:
    v7 = 0
    v8 = f1(v3 - 1, v2 - 1)
    v9 = 1
    v10 = f2(v3 - 1)
    for v6 in range(v4 + 1):
        v7 += v8 * v9
        v7 %= v1
        v8 = v8 * v10 % v1
        v9 = v9 * (v2 - v6 - 1) * v5[v6 + 1] % v1
    v11 = v3 * v7 % v1
    print(v11)

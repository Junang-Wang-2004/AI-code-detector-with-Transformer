def f1(a1, a2, a3=10 ** 9 + 7):
    v1, v2, v3 = (0, a2, [])
    while 2 ** v1 <= a2:
        v1 += 1
    for v4 in range(v1 - 1, -1, -1):
        v3 = [[v4, v2 // 2 ** v4]] + v3
        v2 -= 2 ** v4 * (v2 // 2 ** v4)
    v3[0].append(a1)
    v5 = v3[0][1] * a1 % a3
    for v4 in range(1, v1):
        v3[v4].append(v3[v4 - 1][2] ** 2 % a3)
        if v3[v4][1] == 1:
            v5 = v5 * v3[v4][2] % a3
    return v5

def f2(a1, a2=10 ** 9 + 7):
    v1 = 1
    for v2 in range(1, a1 + 1):
        v1 = v1 * v2 % a2
    return v1

def f3(a1, a2, a3=10 ** 9 + 7):
    v1 = f2(a1 - a2, a3)
    v1 = f1(v1, a3 - 2, a3)
    return v1 * f2(a1, a3) % a3

def f4(a1, a2, a3=10 ** 9 + 7):
    v1 = f2(a1 - a2, a3) * f2(a2, a3) % a3
    v1 = f1(v1, a3 - 2, a3)
    return v1 * f2(a1, a3) % a3
v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = f4(v1 * v2 - 2, v3 - 2, v4)
v6 = 0
for v7 in range(v1):
    v8 = min(abs(v7), abs(v1 - v7 - 1))
    v9 = max(abs(v7), abs(v1 - v7 - 1))
    v6 += v2 ** 2 * (v8 * (v8 + 1) // 2 + v9 * (v9 + 1) // 2)
for v7 in range(v2):
    v8 = min(abs(v7), abs(v2 - v7 - 1))
    v9 = max(abs(v7), abs(v2 - v7 - 1))
    v6 += v1 ** 2 * (v8 * (v8 + 1) // 2 + v9 * (v9 + 1) // 2)
print(v5 * (v6 // 2) % v4)

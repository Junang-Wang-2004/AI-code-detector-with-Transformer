v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7

def f1(a1, a2, a3):
    if a2 > 1:
        return f1(pow(a1, 2) % a3, a2 // 2, a3) * pow(a1, a2 % 2) % a3
    else:
        return a1
v4 = [-1] * (v2 + 1)
for v5 in range(1, v2 + 1):
    if v4[v2 // v5] == -1:
        v4[v2 // v5] = f1(v2 // v5, v1, v3)
v6 = 0
v7 = [0] * (v2 + 1)
for v5 in range(v2, 0, -1):
    v8 = v4[v2 // v5]
    for v9 in range(2, v2 // v5 + 1):
        if v9 > v2 // v5:
            break
        v8 -= v7[v9]
        v8 %= v3
    v7[v5] = v8
    v6 += v8 * v5
    v6 %= v3
print(v6)

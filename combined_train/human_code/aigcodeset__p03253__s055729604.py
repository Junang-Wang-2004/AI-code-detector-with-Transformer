v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4 = v1 + 1000
v5 = [1] * v4
v6 = [1] * v4
for v7 in range(v4 - 1):
    v5[v7 + 1] = v5[v7] * (v7 + 1) % v3
v6[v4 - 1] = pow(v5[v4 - 1], v3 - 2, v3)
for v7 in range(1, v4)[::-1]:
    v6[v7 - 1] = v6[v7] * v7 % v3

def f1(a1, a2):
    return v5[a1] * v6[a1 - a2] % v3 * v6[a2] % v3
v8 = {}
v7 = 2
v9 = v2
while v7 * v7 <= v2:
    if v9 % v7 == 0:
        v8[v7] = 0
        while v9 % v7 == 0:
            v9 = v9 // v7
            v8[v7] += 1
    v7 += 1
if v9 > 1:
    v8[v9] = 1
v10 = 1
for v11 in v8.values():
    v10 *= f1(v11 + v1 - 1, v1 - 1)
    v10 %= v3
print(v10)

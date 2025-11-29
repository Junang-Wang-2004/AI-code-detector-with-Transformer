v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4 = [0] * (v1 + 1)
v5 = [0] * (v1 + 1)
v4[0] = 1
for v6 in range(1, v1 + 1):
    v4[v6] = v4[v6 - 1] * v6 % v3
v5[v1] = pow(v4[v1], v3 - 2, v3)
for v6 in range(v1, 0, -1):
    v5[v6 - 1] = v5[v6] * v6 % v3

def f1(a1, a2):
    return v4[a1] * v5[a2] * v5[a1 - a2] % v3
v7 = 0
for v6 in range(v2 + 1):
    v7 += f1(v1, v6) * f1(v1 - 1, v1 - v6 - 1) % v3
print(v7 % v3)

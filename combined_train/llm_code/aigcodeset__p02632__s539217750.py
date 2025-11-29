v1 = int(input())
v2 = str(input())
v3 = pow(10, 9) + 7
v4 = 2 * pow(10, 6) + 1
v5 = [1] * (v4 + 1)
for v6 in range(1, v4 + 1):
    v5[v6] = v5[v6 - 1] * v6 % v3
v7 = [1] * (v4 + 1)
v7[v4] = pow(v5[v4], v3 - 2, v3)
for v6 in range(v4 - 1, 0, -1):
    v7[v6] = v7[v6 + 1] * (v6 + 1) % v3

def f1(a1, a2):
    if a1 <= 0 or a2 < 0 or a2 > a1:
        return 0
    return v5[a1] * v7[a2] % v3 * v7[a1 - a2] % v3
v8 = len(v2)
v9 = 0
for v6 in range(v1 + 1):
    v9 += pow(25, v6, v3) * pow(26, v1 - v6, v3) * f1(v8 + v6, v8) % v3
print(v9 % v3)

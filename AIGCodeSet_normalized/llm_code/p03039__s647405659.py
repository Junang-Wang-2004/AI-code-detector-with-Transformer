v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = {}

def f1(a1):
    if a1 == 0:
        return 1
    if not a1 in v5:
        v5[a1] = a1 * f1(a1 - 1)
    return v5[a1]
v6 = f1(v1 * v2 - 2) // (f1(v3 - 2) * f1(v1 * v2 - v3))
v7 = 0
for v8 in range(1, v1):
    v7 += v8 * ((v1 - v8) * v2 ** 2) * v6
for v8 in range(1, v2):
    v7 += v8 * ((v2 - v8) * v1 ** 2) * v6
print(v7 % v4)

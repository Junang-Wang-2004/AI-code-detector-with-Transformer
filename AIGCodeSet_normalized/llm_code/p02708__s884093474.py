def f1(a1, a2):
    return a2 * (2 * a1 - a2 + 1) / 2 - a2 * (a2 - 1) / 2 + 1
v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v2, v1 + 2):
    v3 += f1(v1, v4)
print(int(v3 % (10 ** 9 + 7)))

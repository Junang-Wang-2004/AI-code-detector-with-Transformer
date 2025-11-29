from functools import reduce
v1 = 998244353

def f1(a1, a2, a3):
    return 1 if a2 == 0 else reduce(lambda x, y: x * y % a3, range(a1 - a2 + 1, a1 + 1)) * pow(reduce(lambda x, y: x * y % a3, range(1, a2 + 1)), a3 - 2, a3)
v2, v3, v4 = map(int, input().split())
v5 = v3 * pow(v3 - 1, v2 - 1, v1) % v1
v6 = 1
while v6 <= v4 and v6 < v2:
    v7 = (f1(v2, v6, v1) - 1) * v3 * pow(v3 - 1, v2 - v6 - 1, v1) * pow(v3 - 2, v6 - 1, v1) % v1
    v5 += v7
    v6 += 1
print(v5)

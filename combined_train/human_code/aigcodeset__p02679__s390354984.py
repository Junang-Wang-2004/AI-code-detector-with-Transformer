from math import gcd
v1 = int(input())
v2 = 10 ** 9 + 7
v3 = dict()
v4 = 0
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    if not any((v6, v7)):
        v4 += 1
        continue
    if all((v6, v7)):
        v8 = gcd(v6, v7) * (v6 // abs(v6))
    elif v6:
        v8 = v6
    else:
        v8 = v7
    v9 = (v6 // v8, v7 // v8)
    v3[v9] = v3.get(v9, 0) + 1
v10 = 1
v11 = set()
for (v6, v7), v12 in v3.items():
    if (-v7, v6) in v11 or (v7, -v6) in v11:
        continue
    v11.add((v6, v7))
    v13 = v3.get((-v7, v6), 0) + v3.get((v7, -v6), 0)
    v10 *= pow(2, v12) + pow(2, v13) - 1
    v10 %= v2
print((v10 + v4 - 1) % v2)

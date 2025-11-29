from math import gcd
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (v1 + 1)
v4 = [0] * (v1 + 2)
for v5, v6, v7 in zip(v2, v2[::-1], range(1, v1 + 1)):
    v3[v7] = gcd(v5, v3[v7 - 1])
    v4[v1 + 1 - v7] = gcd(v6, v4[v1 - v7 + 2])
v8 = 1
for v7 in range(1, v1 + 1):
    if v7 == 1:
        if v8 < v4[v7 + 1]:
            v8 = v4[v7 + 1]
    elif v7 == v1:
        if v8 < v3[v7 - 1]:
            v8 = v3[v7 - 1]
    elif v8 < gcd(v3[v7 - 1], v4[v7 + 1]):
        v8 = gcd(v3[v7 - 1], v4[v7 + 1])
print(v8)

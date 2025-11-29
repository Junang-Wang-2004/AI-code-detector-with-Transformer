import os, sys, re, math, fractions
v1 = int(input())
v2 = list(map(int, input().split(' ')))
v3 = [1] * v1
v4 = [1] * v1
for v5 in range(v1):
    if v5 == 0:
        v3[v5] = v2[v5]
        v4[v5] = v2[v1 - 1]
    elif v5 == v1 - 1:
        v3[v5] = fractions.gcd(v2[v5], v3[v5 - 1])
        v4[v5] = fractions.gcd(v2[0], v4[v5 - 1])
    else:
        v3[v5] = fractions.gcd(v2[v5], v3[v5 - 1])
        v4[v5] = fractions.gcd(v2[v1 - 1 - v5], v4[v5 - 1])
v4.reverse()
v6 = 1
for v7 in range(v1):
    if v7 == 0:
        v6 = max(v6, v4[1])
    elif v7 == v1 - 1:
        v6 = max(v6, v3[v7 - 1])
    else:
        v8 = fractions.gcd(v3[v7 - 1], v4[v7 + 1])
        v6 = max(v6, v8)
print(v6)

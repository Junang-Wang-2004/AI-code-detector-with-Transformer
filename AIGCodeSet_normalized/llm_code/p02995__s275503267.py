from math import ceil, floor, gcd
v1, v2, v3, v4 = list(map(int, input().split()))
v5 = floor(v2 / v3) - ceil(v1 / v3) + 1
v6 = floor(v2 / v4) - ceil(v1 / v4) + 1
v7 = v3 * v4 // gcd(v3, v4)
v8 = floor(v2 / v7) - ceil(v1 / v7) + 1
v9 = v2 - v1 + 1 - v5 - v6 + v8
print(v9)

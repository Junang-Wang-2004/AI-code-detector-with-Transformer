v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
v5 = v2[0]
v6 = v2[0]
for v7 in range(v1):
    while v4 < v1 - 1 and v5 != v6:
        v4 += 1
        v5 += v2[v4]
        v6 ^= v2[v4]
    if v5 == v6:
        v3 += v4 - v7 + 1
    v5 -= v2[v7]
    v6 ^= v2[v7]
print(v3)

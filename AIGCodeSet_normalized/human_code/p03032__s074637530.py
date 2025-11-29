import bisect
v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v5 = 0
for v6 in range(min(v1, v2) + 1):
    for v7 in range(min(v1, v2) - v6 + 1):
        v8 = 0
        v9 = sorted(v3[:v6] + v3[v1 - v7:])
        v8 = sum(v9[min(v2 - (v6 + v7), bisect.bisect_left(v9, 0)):])
        v5 = max(v5, v8)
print(v5)

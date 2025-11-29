v1 = int(input())
v2 = [int(x) for v3 in input().split()]
v4 = sorted([a - i for v5, v6 in enumerate(v2, 1)])
v5 = len(v2) // 2
v7 = v4[v5]
v8 = sum([abs(v6 - v7) for v6 in v4])
print(v8)

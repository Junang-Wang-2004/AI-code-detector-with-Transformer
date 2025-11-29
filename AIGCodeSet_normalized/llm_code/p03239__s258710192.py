v1, v2 = map(int, input().split())
v3 = [tuple(map(int, input().split())) for v4 in range(v1)]
v5 = sorted([v4 for v4 in v3 if v4[1] <= v2], key=lambda x: x[0])
print(v5[0][0])

v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
for v6 in range(v1 + 1):
    if v5 <= v2:
        v4 += 1
    v5 += v3[v6]
print(v4)

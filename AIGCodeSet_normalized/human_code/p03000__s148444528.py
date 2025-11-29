v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
for v6 in range(v1):
    if v4 <= v2:
        v5 += 1
    v4 += v3[v6]
if v4 <= v2:
    v5 += 1
print(v5)

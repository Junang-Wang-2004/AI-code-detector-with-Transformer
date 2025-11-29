v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    v5 = v2[v4] - (v3 if v4 > 0 else 0)
    if v5 > 0:
        v3 += v5
print(v3)

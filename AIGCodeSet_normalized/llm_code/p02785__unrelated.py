v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v1):
    v4 += v3[v5]
v4 -= v2
if v4 < 0:
    v4 = 0
print(v4)

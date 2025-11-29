v1, v2 = map(int, input().split())
v3 = [0] * v2
v4 = list(map(int, input().split()))
for v5 in range(v2):
    v3[v5] = v4[v5]
print(max(0, max(v3) - (v1 + 1) // 2))

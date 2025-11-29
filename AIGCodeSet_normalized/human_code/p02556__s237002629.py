v1 = int(input())
v2 = [0] * v1
v3 = [0] * v1
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2[v4] = v5 + v6
    v3[v4] = v5 - v6
v7 = max(v2) - min(v2)
v8 = max(v3) - min(v3)
print(max(v7, v8))

v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (v1 // 2)
v3[0] = v2[0]
v3[1] = max(v2[0], v2[1])
for v4 in range(2, v1):
    v3[v4 // 2] = max(v3[(v4 - 2) // 2] + v2[v4], v3[(v4 - 1) // 2])
print(v3[v1 // 2 - 1])

v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v2):
    v4 += max(0, v3[v5] - 1)
print(v4)

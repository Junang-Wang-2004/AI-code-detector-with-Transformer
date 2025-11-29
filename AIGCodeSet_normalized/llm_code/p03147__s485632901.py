v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1 - 1):
    v3 += max(v2[v4 + 1] - v2[v4], 0)
v3 += v2[0]
print(v3)

v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v1):
    v6 = min(v2[v5], v3[v5])
    v4 += v6
    v2[v5] -= v6
    v2[v5 + 1] -= max(0, v6 - v3[v5])
print(v4)

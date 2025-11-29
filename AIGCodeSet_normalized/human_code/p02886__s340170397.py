v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum(v2) ** 2
for v4 in range(v1):
    v3 -= v2[v4] ** 2
print(v3 // 2)

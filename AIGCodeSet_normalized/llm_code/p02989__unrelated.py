v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 0
for v4 in range(v1):
    if v2[v4] <= v2[v1 // 2] and v2[v1 // 2 - 1] < v2[v4]:
        v3 += 1
print(v3)

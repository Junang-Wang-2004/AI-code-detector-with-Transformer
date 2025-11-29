v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sorted(v2)
v4 = 0
for v5 in range(v3[v1 // 2], v3[v1 // 2 - 1], -1):
    if v2.count(v5) % 2 == 0:
        v4 += 1
print(v4)

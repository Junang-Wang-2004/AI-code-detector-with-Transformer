v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum(v2)
v4 = 0
for v5 in v2:
    v4 += v5 * v5
v6 = (v3 * v3 - v4) // 2
print(v6)

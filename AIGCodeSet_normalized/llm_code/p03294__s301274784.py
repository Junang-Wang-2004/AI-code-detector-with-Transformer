v1 = int(input())
v2 = [int(a) for v3 in input().split()]
v4 = 0
for v5 in range(1, max(v2) + 1):
    v6 = 0
    for v3 in v2:
        v6 += v5 % v3
    v4 = max(v4, v6)
print(v4)

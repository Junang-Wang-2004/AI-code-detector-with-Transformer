v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = [int(v3) for v3 in input().split()]
v6 = 0
for v3 in range(v1):
    v6 += v4[v2[v3] - 1]
    if v3 < v1 - 1:
        v6 += v5[min(v2[v3], v2[v3 + 1]) - 1]
print(v6)

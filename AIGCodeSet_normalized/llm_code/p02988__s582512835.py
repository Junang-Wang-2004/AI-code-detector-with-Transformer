v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(1, len(v2) - 1):
    v5 = sorted([v2[v4 - 1], v2[v4], v2[v4 + 1]])
    if v5.index(v2[v4]) == 1:
        v3 += 1
print(v3)

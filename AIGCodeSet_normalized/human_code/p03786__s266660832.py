v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 0
v4 = 0
for v5 in range(len(v2) - 1):
    v3 += v2[v5]
    if v2[v5 + 1] > v3 * 2:
        v4 = v5 + 1
print(len(v2) - v4)

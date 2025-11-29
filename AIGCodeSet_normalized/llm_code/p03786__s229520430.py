v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 0
v4 = 1
v5 = 0
for v6 in range(v1):
    v5 += v2[v6]
    if v6 < v1 - 1 and v5 * 2 < v2[v6 + 1]:
        v3 = v6 + 1
        v4 = 0
    if v4 == 0:
        break
print(v1 - v3)

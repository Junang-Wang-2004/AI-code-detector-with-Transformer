v1 = int(input())
v2 = list(map(int, input().split()))
v2 = [i - 1 for v3 in v2]
v4 = 0
for v3 in range(1, v1):
    if v2[v3 - 1] == v3 - 1:
        v2[v3 - 1], v2[v3] = (v2[v3], v2[v3 - 1])
        v4 += 1
for v3 in reversed(range(1, v1)):
    if v2[v3] == v3:
        v2[v3 - 1], v2[v3] = (v2[v3], v2[v3 - 1])
        v4 += 1
print(v4)

v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4, v5 = (0, 0)
for v3 in range(v1):
    if v2[v3] == v4 + 1:
        v4 += 1
    if v2[v1 - 1 - v3] == v1 - v5:
        v5 += 1
print(v1 - (v4 + v5))

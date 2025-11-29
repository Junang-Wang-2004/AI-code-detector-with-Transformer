v1 = [int(i) for v2 in input().split()]
v3 = []
for v2 in range(v1[0]):
    v3.append(int(input()))
v3.sort()
v4 = abs(v3[0] - v3[v1[1]] - 1)
for v2 in range(v1[1] - 1):
    if v4 > abs(v3[v2] - v3[v2 + v1[1] - 1]):
        v4 = abs(v3[v2] - v3[v2 + v1[1] - 1])
print(v4)

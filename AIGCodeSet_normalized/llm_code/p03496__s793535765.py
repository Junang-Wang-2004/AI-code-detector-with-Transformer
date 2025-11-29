v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = []
v5 = sorted(v2)
if abs(v5[-1]) > abs(v5[0]):
    v6 = v2.index(v5[-1])
    for v3 in range(len(v2) - 1):
        if v2[v3] > v2[v3 + 1]:
            v2[v3 + 1] += abs(v2[v3 + 1] - v2[v3]) // abs(v5[-1]) + 1
            v4.extend([str(v6 + 1) + ' ' + str(v3 + 2)] * (abs(v2[v3 + 1] - v2[v3]) // abs(v5[-1]) + 1))
else:
    v7 = v2.index(v5[0])
    for v3 in range(len(v2) - 1, 0, -1):
        if v2[v3] < v2[v3 - 1]:
            v2[v3] += abs(v2[v3 - 1] - v2[v3]) // abs(v5[0]) + 1
            v4.extend([str(v7 + 1) + ' ' + str(v3)] * (abs(v2[v3 - 1] - v2[v3]) // abs(v5[0]) + 1))
print(len(v4))
for v3 in v4:
    print(v3)

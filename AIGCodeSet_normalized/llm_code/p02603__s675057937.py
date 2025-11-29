import copy, sys
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = copy(v2)
for v4 in range(v1 - 1):
    if v3[v4] == v2[v4 + 1]:
        v3.pop(v4)
if not v3:
    print(1000)
    sys.exit()
v5 = [v3[0]]
for v4 in range(1, len(v3) - 1):
    if not (v3[v4 - 1] < v3[v4] < v3[v4 + 1] or v3[v4 - 1] > v3[v4] > v3[v4 + 1]):
        v5.append(v3[v4])
v5.append(v3[-1])
v6 = 1000
v7 = 0
v8 = len(v5)
for v4 in range(v8 - 1):
    if v5[v4] > v5[v4 + 1]:
        v6 += v5[v4] * v7
        v7 = 0
    elif v6 > 0:
        v7, v6 = divmod(v6, v5[v4])
if len(v5) > 1 and v5[-1] > v5[-2]:
    v6 += v5[-1] * v7
print(v6)

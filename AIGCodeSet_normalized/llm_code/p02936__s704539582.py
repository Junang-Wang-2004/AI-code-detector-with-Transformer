import collections
v1, v2 = [int(i) for v3 in input().split()]
v4 = [0] * (v1 + 1)
v5 = [[] for v6 in range(v1 + 1)]
for v6 in range(v1 - 1):
    v7, v8 = [int(v3) for v3 in input().split()]
    v5[v7].append(v8)
    v5[v8].append(v7)

def f1(a1, a2):
    for v1 in v5[a1]:
        if v1 != a2:
            v4[v1] += v4[a1]
            f1(v1, a1)
for v6 in range(v2):
    v9, v10 = [int(v3) for v3 in input().split()]
    v4[v9] += v10
f1(1, 0)
print(*v4[1:v1 + 1])

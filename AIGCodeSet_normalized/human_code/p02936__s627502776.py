from collections import defaultdict

def f1(a1, a2, a3, a4):
    v1 = [a1]
    while len(v1) > 0:
        v2 = v1.pop()
        v3 = a4[v2]
        for v4 in a3[v2]:
            if a2[v4] == 0:
                a2[v4] = 1
                a4[v4] += v3
                v1.append(v4)
    return (a2, a4)
v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v1 + 1)]
v5 = [[] for v4 in range(v1 + 1)]
for v6 in range(v1 - 1):
    v7, v8 = map(int, input().split())
    v5[v7].append(v8)
    v5[v8].append(v7)
v9 = [0 for v4 in range(v1 + 1)]
for v6 in range(v2):
    v10, v11 = map(int, input().split())
    v9[v10] += v11
v3[1] = 1
f1(1, v3, v5, v9)
print(*v9[1:])

def f1(a1, a2=-1):
    global ans
    v1 = 0
    for v2 in graph[a1]:
        if v2 != a2:
            v1 += f1(v2, a1)
    if a1 != 1 and a1 != N:
        if v1 % 2 == 0:
            v3 = 'Snuke'
        else:
            v3 = 'Fennec'
    return v1 + 1
v1 = int(input())
v2 = [[] for v3 in range(v1 + 1)]
for v3 in range(v1 - 1):
    v4, v5 = map(int, input().split())
    v2[v4].append(v5)
    v2[v5].append(v4)
v6 = 'Fennec'
f1(1)
print(v6)

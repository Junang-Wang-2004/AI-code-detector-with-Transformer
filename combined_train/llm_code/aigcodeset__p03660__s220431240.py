from collections import deque
v1 = int(input())
v2 = [[] for v3 in range(v1)]
for v3 in range(v1 - 1):
    v4, v5 = map(int, input().split())
    v2[v4 - 1] += [v5 - 1]
    v2[v5 - 1] += [v4 - 1]

def f1(a1, a2, a3):
    v1 = deque([a2])
    v2 = [-1] * v1
    while v1:
        v3 = v1.popleft()
        for v4 in a1[v3]:
            if v4 == v2[v3]:
                continue
            v2[v4] = v3
            if v4 == a3:
                break
            v1.append(v4)
    return v2
v6 = f1(v2, 0, v1 - 1)
v7 = [v1 - 1]
while v7[0] != 0:
    v7 = [v6[v7[0]]] + v7
v8 = (len(v7) - 1) // 2
v9 = v7[v8]
v10 = v7[v8 + 1]
v2[v9].remove(v10)

def f2(a1, a2):
    v1 = deque([a2])
    v2 = [-1] * v1
    while v1:
        v3 = v1.popleft()
        for v4 in a1[v3]:
            if v2[v4] == v3:
                continue
            v2[v4] = v3
            v1.append(v4)
    v5 = sum([v3 for v3 in v2 if v3 != -1]) + 1
    return v5
v11 = f2(v2, 0)
v12 = v1 - v11
if v11 > v12:
    print('Fennec')
else:
    print('Snuke')

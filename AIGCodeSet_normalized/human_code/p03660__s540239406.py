import sys
sys.setrecursionlimit(600000)
v1 = int(input())
v2 = [[] for v3 in range(v1)]
for v3 in range(v1 - 1):
    v4, v5 = map(int, input().split())
    v2[v4 - 1].append(v5 - 1)
    v2[v5 - 1].append(v4 - 1)

def f1(a1, a2, a3):
    if a1 == v1 - 1:
        return (a3, True)
    v1 = False
    for v2 in v2[a1]:
        if not a2[v2]:
            a3.append(v2)
            a2[v2] = True
            v3, v4 = f1(v2, a2, a3)
            if v4:
                v5 = v3
                v1 = True
    if not v1:
        a3.pop()
        return (a3, False)
    return (v5, True)
v6 = [False for v3 in range(v1)]
v6[0] = True
v7, v8 = f1(0, v6, [0])
v9 = [0 for v3 in range(v1)]
v10 = len(v7)
if v10 % 2 == 0:
    v11 = v7[v10 // 2 - 1]
    v12 = v7[v10 // 2]
else:
    v11 = v7[v10 // 2]
    v12 = v7[v10 // 2 + 1]
v9[v11] = True
v9[v12] = True

def f2(a1, a2, a3):
    a3 += 1
    for v2 in v2[a1]:
        if not a2[v2]:
            a2[v2] = True
            a3 = f2(v2, a2, a3)
    return a3
v13 = f2(v11, v9, 0)
v14 = f2(v12, v9, 0)
if v14 < v13:
    print('Fennec')
else:
    print('Snuke')

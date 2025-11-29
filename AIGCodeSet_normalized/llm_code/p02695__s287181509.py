v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v3):
    v6, v7, v8, v9 = map(int, input().split())
    v4.append((v6, v7, v8, v9))
v10 = 0
v11 = []
sys.setrecursionlimit(10 ** 6)

def f1(a1):
    if len(a1) == v1:
        v11.append(a1)
    else:
        for v1 in range(v2 - a1[-1] + 1):
            f1(a1 + [a1[-1] + v1])
f1([1])
for v12 in v11:
    v13 = 0
    for v14 in range(v3):
        if v12[v4[v14][1] - 1] - v12[v4[v14][0] - 1] == v4[v14][2]:
            v13 += v4[v14][3]
    v10 = max(v10, v13)
print(v10)

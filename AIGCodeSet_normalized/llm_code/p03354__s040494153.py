v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [list(map(int, input().split())) for v5 in range(v2)]
v6 = [i for v7 in range(v1 + 1)]
v8 = [0] * (v1 + 1)

def f1(a1):
    if v6[a1] != a1:
        v6[a1] = f1(v6[a1])
    return v6[a1]

def f2(a1, a2):
    v1 = f1(a1)
    v2 = f1(a2)
    if v1 != v2:
        if v8[v1] < v8[v2]:
            v6[v1] = v2
        elif v8[v1] > v8[v2]:
            v6[v2] = v1
        else:
            v6[v2] = v1
            v8[v1] += 1
for v9 in v4:
    f2(v9[0], v9[1])
v10 = 0
for v7 in range(v1):
    if f1(v3[v7]) == f1(v7 + 1):
        v10 += 1
print(v10)

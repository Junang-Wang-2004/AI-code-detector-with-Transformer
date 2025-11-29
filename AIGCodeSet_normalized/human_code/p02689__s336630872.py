v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [True for v5 in range(v1)]
v6 = v1
for v5 in range(v2):
    v7, v8 = map(int, input().split())
    v7 -= 1
    v8 -= 1
    if v3[v7] > v3[v8]:
        if v4[v8]:
            v6 -= 1
        v4[v8] = False
    elif v3[v7] < v3[v8]:
        if v4[v7]:
            v6 -= 1
        v4[v7] = False
    else:
        if v4[v7]:
            v6 -= 1
        v4[v7] = False
        if v4[v8]:
            v6 -= 1
        v4[v8] = False
print(v6)

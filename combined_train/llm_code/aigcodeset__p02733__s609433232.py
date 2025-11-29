v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, list(input()))) for v5 in range(v1)]
v6 = v1 * v2

def f1(a1, a2, a3, a4):
    v1 = sum([sum(s[a3:a4]) for v2 in v4[a1:a2]])
    return v1
for v7 in range(1 << v1 - 1):
    v8 = 0
    v9 = [0]
    for v10 in range(v1):
        if v7 >> v10 & 1:
            v9.append(v10 + 1)
            v8 += 1
    v9.append(v1)
    if v8 > v6:
        continue
    v11 = 0
    for v12 in range(1, v2 + 1):
        v13 = 0
        for v10 in range(len(v9) - 1):
            v13 = max(v13, f1(v9[v10], v9[v10 + 1], v11, v12))
        if v13 > v3:
            v11 = v12
            v8 += 1
            if v8 > v6:
                break
    else:
        if v8 < v6:
            v6 = v8
print(v6)

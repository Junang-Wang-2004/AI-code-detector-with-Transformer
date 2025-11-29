def f1():
    v1 = int(input())
    v2 = []
    v3 = {i: 0 for v4 in range(v1)}
    for v4 in range(v1 - 1):
        v5, v6 = [int(n) for v7 in input().split()]
        v5, v6 = (v5 - 1, v6 - 1)
        v2.append((v5, v6))
        v3[v5] += 1
        v3[v6] += 1
    v8 = [int(v7) for v7 in input().split()]
    v8.sort()
    v9 = [0] * v1
    for v10, v11 in enumerate(sorted(list(v3.items()), key=lambda x: x[1])):
        v9[v11[0]] = v8[v10]
    v12 = 0
    for v13 in v2:
        v12 += min(v9[v13[0]], v9[v13[1]])
    print(v12)
    print(' '.join([str(v4) for v4 in v9]))
f1()

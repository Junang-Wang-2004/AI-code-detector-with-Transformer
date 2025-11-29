def f1(a1, a2):
    for v1 in range(len(a1)):
        for v2 in range(len(a1[0])):
            if a1[v1][v2] == a2:
                return (v1, v2)
    return None
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(list(map(int, input().split())))
v6 = int(input())
for v5 in range(v6):
    v7, v8 = map(int, input().split())
    v9 = 0
    v10 = v7
    v11 = f1(v4, v10)
    while v10 != v8:
        v12 = v10 + v3
        v13 = f1(v4, v12)
        v9 += abs(v11[0] - v13[0]) + abs(v11[1] - v13[1])
        v10 = v12
        v11 = v13
    print(v9)

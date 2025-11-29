v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(input())
v5 = [0, 0, 1, -1]
v6 = [1, -1, 0, 0]

def f1(a1, a2):
    global check
    global was
    was[a1][a2] = 1
    if v3[a1][a2] == '#':
        check[0] += 1
    else:
        check[1] += 1
    for v1 in range(4):
        v2 = a2 + v5[v1]
        v3 = a1 + v6[v1]
        if 0 <= v3 < v1 and 0 <= v2 < v2 and (v3[v3][v2] != v3[a1][a2]) and (not was[v3][v2]):
            f1(v3, v2)
v7 = 0
v8 = [[0 for v4 in range(v2)] for v9 in range(v1)]
for v4 in range(v1):
    for v9 in range(v2):
        if not v8[v4][v9]:
            v10 = [0, 0]
            f1(v4, v9)
            v7 += v10[0] * v10[1]
print(v7)

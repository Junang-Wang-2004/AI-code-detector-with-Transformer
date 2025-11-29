v1, v2 = map(int, input().split())
v3 = [0] * v1
v4 = [0] * v1
for v5 in range(v1):
    v3[v5], v4[v5] = map(int, input().split())
v6 = [0] + v3
v7 = [0] + v4
v8 = [0] + list(map(lambda a: v2 - a, v3[::-1]))
v9 = [0] + v4[::-1]
v10 = [0] * (v1 + 1)
v11 = [0] * (v1 + 1)
v10[0] = v11[0] = (0, 0)

def f1(a1, a2, a3):
    v1 = v2 = v3 = 0
    for v4 in range(1, v1 + 1):
        v5 = a2[v4] - a2[v4 - 1]
        v3 += a3[v4] - v5
        if v3 > v1:
            v1 = v3
            v2 = a2[v4]
        a1[v4] = (v1, v2)
f1(v10, v6, v7)
f1(v11, v8, v9)
v12 = 0
for v5 in range(v1 + 1):
    v12 = max(v12, v10[v5][0] + v11[v1 - v5][0] - min(v10[v5][1], v11[v1 - v5][1]))
print(v12)

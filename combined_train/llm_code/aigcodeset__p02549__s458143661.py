v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v1)]
v5 = [-1 for v4 in range(v1)]
min = v1
for v4 in range(v2):
    v6, v7 = map(int, input().split())
    if v6 < min:
        min = v6
    for v8 in range(v6 - 1, v7):
        v3[v8] = 1
for v8 in range(min - 1):
    v5[v8] = 0
v5[min - 1] = 1

def f1(a1, a2, a3):
    v1 = 0
    for v2 in range(0, a1 - 1):
        if a2[v2] == 1:
            if a3[a1 - v2 - 2] == -1:
                a3 = f1(a1 - v2 - 1, a2, a3)
            v1 += a3[a1 - v2 - 2]
    a3[a1 - 1] = v1
    return a3
v5 = f1(v1, v3, v5)
v9 = v5[-1]
print(v9 % 998244353)

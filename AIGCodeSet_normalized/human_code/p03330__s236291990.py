v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]

def f1():
    v1 = []
    v2 = []
    v3 = []
    for v4 in range(1, v2 + 1):
        v5 = 0
        for v6 in range(v1):
            for v7 in range(v1):
                if (v6 + v7) % 3 == 0:
                    v5 += v3[v5[v6][v7] - 1][v4 - 1]
        v1.append(v5)
    for v4 in range(1, v2 + 1):
        v5 = 0
        for v6 in range(v1):
            for v7 in range(v1):
                if (v6 + v7) % 3 == 1:
                    v5 += v3[v5[v6][v7] - 1][v4 - 1]
        v2.append(v5)
    for v4 in range(1, v2 + 1):
        v5 = 0
        for v6 in range(v1):
            for v7 in range(v1):
                if (v6 + v7) % 3 == 2:
                    v5 += v3[v5[v6][v7] - 1][v4 - 1]
        v3.append(v5)
    return (v1, v2, v3)
v6 = 10 ** 18
v7, v8, v9 = f1()
for v10, v11 in enumerate(v7):
    for v12, v13 in enumerate(v8):
        for v14, v15 in enumerate(v9):
            if v10 != v12 and v12 != v14 and (v14 != v10):
                v6 = min(v11 + v13 + v15, v6)
print(v6)

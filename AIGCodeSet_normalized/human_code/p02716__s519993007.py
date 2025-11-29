v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1):
    if a1 % 2 == 0:
        return (v1 - a1) // 2 + 1
    else:
        return (v1 - a1 - 1) // 2 + 1
v3 = [{} for v4 in range(v1)]
for v4 in range(v1):
    if v4 < 2:
        v3[v4][0] = 0
        v3[v4][1] = v2[v4]
    else:
        v5 = f1(v4 + 2)
        v6 = v4 - 2
        while v6 >= 0:
            v7 = max(v3[v6].keys())
            if v7 + v5 + 1 < v1 // 2:
                break
            else:
                for v8, v9 in v3[v6].items():
                    if v8 + v5 + 1 >= v1 // 2:
                        if v8 + 1 in v3[v4]:
                            v3[v4][v8 + 1] = max(v3[v4][v8 + 1], v9 + v2[v4])
                        else:
                            v3[v4][v8 + 1] = v9 + v2[v4]
            v6 -= 1
        if 1 + v5 >= v1 // 2:
            v3[v4][0] = 0
v10 = None
for v4 in range(v1):
    for v8, v11 in v3[v4].items():
        if v8 == v1 // 2:
            if v10 is None:
                v10 = v11
            else:
                v10 = max(v10, v11)
print(v10)

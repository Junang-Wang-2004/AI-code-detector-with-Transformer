v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
v6 = []
v7 = []
v8 = 0
if v3[0] < 0:
    for v9 in range(v1):
        if v3[v9] >= 0:
            v8 = v9
            break
    v6 = v3[:v8]
    v6 = v6[::-1]
    for v9 in range(len(v6)):
        v6[v9] = abs(v6[v9])
    v7 = v3[v8:]
    v10 = 10000000000000000
    v11 = len(v6)
    v12 = len(v7)
    for v9 in range(v11):
        if v2 - (v9 + 1) <= v12 and v2 - (v9 + 1) >= 0:
            v10 = min(v10, v6[v9] * 2 + v7[v2 - 1 - (v9 + 1)])
    for v9 in range(v12):
        if v2 - (v9 + 1) <= v11 and v2 - (v9 + 1) >= 0:
            v10 = min(v10, v7[v9] * 2 + v6[v2 - 1 - (v9 + 1)])
    if v2 - 1 < v11:
        v10 = min(v10, v6[v2 - 1])
    if v2 - 1 < v12:
        v10 = min(v10, v7[v2 - 1])
    print(v10)
else:
    print(v3[v2 - 1])

v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 10 ** 9 + 7
v5 = sorted([i for v6 in v3 if v6 < 0], reverse=True)
v7 = sorted([v6 for v6 in v3 if v6 >= 0])
v8, v9 = (1, [])
if len(v7) == 0 and v2 % 2 == 1:
    for v6 in v5[:v2]:
        v8 = v8 * v6 % v4
    print(v8)
    exit()
for v10 in range(v2):
    if len(v5) > 0 and len(v7) > 0:
        if abs(v5[-1]) <= v7[-1]:
            v11 = v7.pop()
        elif abs(v5[-1]) > v7[-1]:
            v11 = v5.pop()
    elif len(v5) == 0:
        v11 = v7.pop()
    elif len(v7) == 0:
        v11 = v5.pop()
    v9.append(v11)
v12 = sum((v6 < 0 for v6 in v9))
for v6 in v9:
    v8 = v8 * v6 % v4
if v12 % 2 == 1:
    v13, v14, v15, v16 = (1, 0, -1, 0)
    if len(v5) > 0 and v12 != v2:
        v13, v14 = (min((v6 for v6 in v9 if v6 >= 0)), v5[-1])
    if len(v7) > 0:
        for v6 in v9[::-1]:
            if v6 < 0:
                v15, v16 = (v6, v7[-1])
                break
    if len(v5) > 0 or (len(v7) > 0 and v12 != v2):
        if v14 * v15 >= v13 * v16:
            v8 *= v14 * pow(v13, v4 - 2, v4)
        if v14 * v15 < v13 * v16:
            v8 *= v16 * pow(v15, v4 - 2, v4)
    v8 %= v4
print(v8)

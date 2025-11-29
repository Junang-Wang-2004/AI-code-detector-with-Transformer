v1 = int(input())
v2 = [int(s) for v3 in input().split(' ')]
v4 = {}
for v5 in v2:
    if v5 in v4:
        v4[v5] += 1
    else:
        v4[v5] = 1
v6 = list(v4.keys())
v7 = len(v6)
if v1 < 3:
    v8 = False
else:
    v8 = False
    if 0 in v6:
        for v9, v10 in v4.items():
            if v10 >= 2 and v9 != 0:
                v8 = True
                break
    if not v8:
        for v11 in range(v7):
            for v12 in range(v11 + 1, v7):
                v13 = v6[v11] ^ v6[v12]
                if v13 in v6 and v13 != v6[v11] and (v13 != v6[v12]) and (v4[v13] >= 2):
                    v8 = True
                    break
            if v8:
                break
print('Yes' if v8 else 'No')

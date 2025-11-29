v1, v2 = map(int, input().split())
v3 = [list(input().split()) for v4 in range(v2)]
v5 = []
v6 = v7 = 0
for v8 in v3:
    if v8[0] not in v5:
        if v8[1] == 'WA':
            v7 += 1
        else:
            v6 += 1
            v5.append(v8[0])
print(v6, v7)

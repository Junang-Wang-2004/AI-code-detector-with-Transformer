v1, v2 = map(int, input().split())
v3 = input()
v4 = [[] for v5 in range(v1 + 1)]
v4[0] = [0]
v6 = 0
v7 = [0] + [-1] * v1
v8 = 1
while v8 <= v1:
    v9 = v4[v6]
    if not v9:
        break
    for v10 in v9:
        v11 = min(v10 + v2 + 1, v1 + 1)
        for v5 in range(v8, v11):
            if v3[v5] == '0':
                v4[v6 + 1].append(v5)
                v7[v5] = v10
        v8 = v11
    v6 += 1
if v7[v1] == -1:
    v12 = -1
else:
    v8 = v1
    v12 = []
    while v8 > 0:
        v13 = v7[v8]
        v12.append(str(v8 - v13))
        v8 = v13
    v12 = v12[::-1]
    v12 = ' '.join(v12)
print(v12)

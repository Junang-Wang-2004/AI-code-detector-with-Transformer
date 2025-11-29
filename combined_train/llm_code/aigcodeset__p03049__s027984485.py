v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(input())
v4 = 0
for v5 in v2:
    v4 += v5.count('AB')
v6 = [list(s) for v7 in v2]
v8 = 0
v9 = 0
v10 = 0
for v11 in v6:
    if v11[0] == 'B':
        v8 += 1
    if v11[-1] == 'A':
        v9 += 1
        if v11[0] == 'B':
            v10 += 1
v12 = min(v9, v8)
if v12 == v10:
    if v12 != 0:
        v12 -= 1
print(v4 + v12)

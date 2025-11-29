v1 = int(input())
v2 = []
v3 = []
v4 = 0
for v5 in range(v1):
    v6 = input()
    v7 = 0
    v8 = 0
    for v9 in range(len(v6)):
        if v6[v9] == '(':
            v7 = v7 + 1
        else:
            v7 = v7 - 1
            if v7 < 0:
                v8 = max(v8, -v7)
    if v8 == 0:
        v4 = v4 + v7
    elif v7 > 0:
        v3.append([v8, -1 * v7])
    else:
        v2.append([-1 * v8, v7])
v2.sort()
v3.sort()
v10 = 0
for v5 in range(len(v3)):
    if v4 + v3[v5][0] < 0:
        v10 = 1
    v4 = v4 - v3[v5][1]
for v5 in range(len(v2)):
    if v4 - v2[v5][0] < 0:
        v10 = 1
    v4 = v4 + v2[v5][1]
if v4 != 0:
    v10 = 1
if v10 == 0:
    print('Yes')
else:
    print('No')

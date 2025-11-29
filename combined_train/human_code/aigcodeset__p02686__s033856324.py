import sys
v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5 = input()
    v6 = 0
    v7 = 0
    v8 = 0
    for v9 in range(len(v5)):
        if v5[v9] == '(':
            v8 += 1
        else:
            v8 -= 1
        v7 = min(v8, v7)
    v6 = v8
    if v6 >= 0:
        v2.append([v6, v7])
    else:
        v3.append([v6, v7])
v10 = 0
v2 = sorted(v2, key=lambda t: t[1])
v2.reverse()
v3 = sorted(v3, key=lambda t: t[0] - t[1])
v3.reverse()
for v4 in v2:
    if v10 + v4[1] < 0:
        print('No')
        sys.exit()
    v10 += v4[0]
for v4 in v3:
    if v10 + v4[1] < 0:
        print('No')
        sys.exit()
    v10 += v4[0]
if v10 == 0:
    print('Yes')
else:
    print('No')

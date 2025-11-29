import sys
input = sys.stdin.readline
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = input().rstrip()
    v5 = v4.count('(')
    v6 = v4.count(')')
    v7 = 0
    v8 = 0
    for v9 in range(len(v4)):
        if v4[v9] == '(':
            v8 += 1
        else:
            v8 -= 1
            v7 = min(v7, v8)
    v2.append((v5, v6, v4, v7))
v2.sort(key=lambda x: x[1] - x[0])
v10 = []
v7 = []
v11 = []
for v12 in v2:
    if v12[3] >= 0:
        v11.append(v12)
    elif v12[0] - v12[1] > 0:
        v10.append(v12)
    else:
        v7.append(v12)
v10.sort(key=lambda x: -v12[3])
v7.sort(key=lambda x: -(v12[0] - v12[1] - v12[3]))
v5 = v6 = 0
for v12 in v11 + v10 + v7:
    for v3 in range(len(v12[2])):
        if v12[2][v3] == '(':
            v5 += 1
        else:
            v6 += 1
        if v5 < v6:
            print('No')
            exit()
if v5 == v6:
    print('Yes')
else:
    print('No')

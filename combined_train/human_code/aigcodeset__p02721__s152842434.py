v1 = input().split()
v2 = int(v1[1])
v3 = int(v1[2])
v4 = input()
v5 = []
for v6, v7 in enumerate(v4):
    if v7 == 'o':
        v5.append(v6 + 1)
v4 = 1
v8 = 0
v9 = 1
v10 = []
v10.append(v5[0])
while v4 < v2:
    if v9 >= len(v5):
        break
    elif v5[v9] - v5[v8] > v3:
        v8 = v9
        v10.append(v5[v9])
        v4 += 1
    else:
        v9 = v9 + 1
v11 = 1
v12 = len(v5) - 1
v13 = len(v5) - 2
v14 = []
v14.append(v5[-1])
while v11 < v2:
    if v13 < 0:
        break
    elif v5[v12] - v5[v13] > v3:
        v12 = v13
        v14.append(v5[v13])
        v11 += 1
    else:
        v13 = v13 - 1
v14.reverse()
v15 = True
for v6 in range(len(v10)):
    if v10[v6] == v14[v6]:
        v15 = False
        print(v10[v6])
if v15:
    print()

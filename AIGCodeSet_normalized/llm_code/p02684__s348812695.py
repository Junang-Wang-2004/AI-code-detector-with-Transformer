import sys
v1 = sys.stdin
v2 = lambda: v1.readline().rstrip()
v3 = lambda: int(v1.readline().rstrip())
v4 = lambda: map(int, v1.readline().split())
v5 = lambda: list(map(int, v1.readline().split()))
v6, v7 = v4()
v8 = v5()
v9 = []
v9.append(1)
v10 = [0] * (v6 + 1)
v10[1] += 1
v11 = v8[0]
v12 = True
v13 = -1
v14 = -1
while v12:
    v10[v11] += 1
    v9.append(v11)
    if v10[v11] > 1:
        v13 = v9.index(v11)
        v14 = len(v9) - 1
        v12 = False
    v11 = v8[v11 - 1]
if v7 <= v14:
    print(v9[v7])
else:
    v15 = v7 - v14
    v15 = v15 % (v14 - v13 + 1)
    print(v9[v13 + v15])

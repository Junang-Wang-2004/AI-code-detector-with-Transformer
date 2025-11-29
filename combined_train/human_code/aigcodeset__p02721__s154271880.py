import sys
v1 = sys.stdin.readline
v2, v3, v4 = map(int, v1().split())
v5 = v1().rstrip()
v6 = 'o'
v7 = 'x'
v8 = [None] * v2
v9 = 0
v10 = 0
while True:
    v11 = v9
    while v11 < v2:
        if v5[v11] == v6:
            v9 = v11 + v4 + 1
            v8[v11] = 1
            v10 += 1
            break
        v11 += 1
    if v11 >= v2:
        break
if v10 > v3:
    exit(0)
v12 = [None] * v2
v10 = 0
v9 = v2 - 1
while True:
    v11 = v9
    while v11 > -1:
        if v5[v11] == v6:
            v9 = v11 - v4 - 1
            v12[v11] = 1
            v10 += 1
            break
        v11 -= 1
    if v11 <= -1:
        break
for v11 in range(v2):
    if v8[v11] == 1 and v12[v11] == 1:
        print(v11 + 1)

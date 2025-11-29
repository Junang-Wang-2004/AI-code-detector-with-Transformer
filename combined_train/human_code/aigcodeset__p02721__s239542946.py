v1, v2, v3 = map(int, input().split())
v4 = input()
v5 = [0] * v2
v6 = [0] * v2
v7 = 0
v8 = 0
while v8 < v1:
    if v4[v8] == 'o':
        v5[v7] = v8
        v7 += 1
        if v7 >= v2:
            break
        v8 += v3
    v8 += 1
v7 = v2 - 1
v8 = v1 - 1
while v8 >= 0:
    if v4[v8] == 'o':
        v6[v7] = v8
        v7 -= 1
        if v7 < 0:
            break
        v8 -= v3
    v8 -= 1
for v8 in range(v2):
    if v5[v8] == v6[v8]:
        print(v5[v8] + 1)

v1, v2, v3 = map(int, input().split())
v4 = list(input())
v5 = list()
v6 = list()
v7 = 0
v8 = 0
while v8 < v2:
    if v4[v7] == 'o':
        v5.append(v7)
        v8 += 1
        v7 += v3
    v7 += 1
v7 = len(v4) - 1
v8 = 0
while v8 < v2:
    if v4[v7] == 'o':
        v6.append(v7)
        v8 += 1
        v7 -= v3
    v7 -= 1
v6.sort()
for v7, v9 in zip(v5, v6):
    if v7 == v9:
        print(v7 + 1)

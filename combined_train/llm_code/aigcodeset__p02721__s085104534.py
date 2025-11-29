v1, v2, v3 = list(map(int, input().split()))
v4 = input()
v5 = set()
v6 = set()
v7 = 0
v8 = 0
while v7 < v3 and v8 < v3:
    if v4[v7] == 'o':
        v5.add(v7 + 1)
        v7 += v3 + 1
        v8 += 1
        continue
    v7 += 1
v7 = v1 - 1
v8 = 0
while v7 < v3 and v8 < v3:
    if v4[v7] == 'o':
        v6.add(v7 + 1)
        v7 -= v3 + 1
        v8 += 1
        continue
    v7 -= 1
v9 = v5 & v6
for v10 in sorted(v9):
    print(v10)

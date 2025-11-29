def f1(a1, a2):
    if a1 == 0:
        return a2
    return f1(a2 % a1, a1)
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v2.sort()
for v4 in v2:
    v3 = f1(v3, v4)
if v3 != 1:
    print('not coprime')
    exit()
v5 = []
v6 = [True] * 1100000
v6[0] = v6[1] = False
for v7 in range(2, 1100000):
    if not v6[v7]:
        continue
    for v8 in range(v7 * v7, 1100000, v7):
        v6[v8] = False
    v5.append(v7)
v9 = [v4 for v4 in v2 if v6[v4]]
v10 = [v4 for v4 in v2 if not v6[v4]]
v5 = [p for v11 in range(1100) if v6[v11]]
v12 = [False] * 1100000
for v4 in v9:
    v12[v4] = True
for v13 in v10:
    for v11 in v5:
        if v13 == 1:
            break
        if v13 % v11 != 0:
            continue
        if v12[v11]:
            print('setwise coprime')
            exit()
        v12[v11] = True
        while v13 % v11 == 0:
            v13 //= v11
    if v13 > 1:
        print('not coprime')
        exit()
print('pairwise coprime')

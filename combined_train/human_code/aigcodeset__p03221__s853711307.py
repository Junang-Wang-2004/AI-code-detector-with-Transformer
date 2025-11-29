from operator import itemgetter
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) + [i] for v4 in range(v2)]
v3.sort(key=itemgetter(1))
v3.sort(key=itemgetter(0))
v5 = 0
v6 = 0
v7 = 1
while v6 < v2:
    if v3[v6][0] == v5:
        v3[v6][1] = v7
        v7 += 1
        v6 += 1
    else:
        v5 += 1
        v7 = 1
        continue
v3.sort(key=itemgetter(2))
for v4 in range(v2):
    print(str(v3[v4][0]).zfill(6) + str(v3[v4][1]).zfill(6))

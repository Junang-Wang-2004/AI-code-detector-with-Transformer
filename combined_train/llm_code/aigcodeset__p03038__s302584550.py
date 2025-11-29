v1, v2 = map(int, input().split())
v3 = sorted(list(map(int, input().split())))
v4 = []
for v5 in range(2):
    v6, v7 = map(int, input().split())
    v4.append([v6, v7])
from operator import itemgetter
v4.sort(key=itemgetter(1))
v8 = 0
v7 = v4[0][1]
v6 = v4[0][1]
v9 = 0
while v3[v8] < v7:
    v3[v8] = v7
    v8 += 1
    if v8 >= len(v3):
        break
    v6 -= 1
    if v6 == 0:
        v9 += 1
        if v9 > len(v4):
            break
        v6 = v4[v9][0]
        v7 = v4[v9][1]
print(sum(v3))

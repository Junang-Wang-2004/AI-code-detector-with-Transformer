from operator import itemgetter
v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append([v5, v6])
for v4 in range(v1):
    v7, v8 = map(int, input().split())
    v3.append([v7, v8])
v3 = sorted(v3)
v2 = sorted(v2, key=itemgetter(1), reverse=True)
v9 = 0
for v4 in v3:
    for v10 in v2:
        if v4[0] > v10[0] and v4[1] > v10[1]:
            v9 += 1
            v2.remove(v10)
            break
print(v9)

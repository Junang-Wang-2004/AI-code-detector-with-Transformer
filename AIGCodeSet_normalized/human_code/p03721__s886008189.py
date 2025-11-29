v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(list(map(int, input().split())))
v3.sort()
v5 = 0
v6 = 0
for v4 in range(v1):
    v5 += v3[v4][1]
    if v5 >= v2:
        v6 = v4
        break
print(v3[v6][0])

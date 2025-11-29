v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = 0
v5 = 0
v6 = [x for v7 in zip(*v2)]
for v8 in range(v1):
    if v6[0][v8] >= v6[1][v8]:
        v4 += v6[0][v8]
    else:
        v5 += v6[1][v8]
v9 = v4 - v5
print(str(v9))

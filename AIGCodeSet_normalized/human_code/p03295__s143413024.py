v1, v2 = map(int, input().split())
v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
v3.sort(key=lambda x: x[1])
v5 = 0
v6 = -1
for v7, v8 in v3:
    if v7 >= v6:
        v5 += 1
        v6 = v8
print(v5)

v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v3.sort()
v5 = 1
v6 = v3[0][0]
v7 = v3[0][1]
for v8, v9 in v3:
    if v7 <= v8 or v6 >= v9:
        v5 += 1
        v6 = v8
        v7 = v9
    else:
        v6 = v8
        v7 = min(v7, v9)
print(v5)

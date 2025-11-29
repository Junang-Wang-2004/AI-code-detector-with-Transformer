v1 = map(int, input().split())
v2 = list(v1)
v3 = v2[0]
v4 = v2[1]
v5 = v2[2]
v6 = v2[3]
v7 = v5 - v3
v8 = v6 - v4
v9 = v5 - v8
v10 = v6 + v7
v11 = v3 - v8
v12 = v4 + v7
v13 = [v9, v10, v11, v12]
print(*v13)

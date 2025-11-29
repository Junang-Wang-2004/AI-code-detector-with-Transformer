v1, v2 = map(int, input().split())
v3 = input().split()
v3 = [int(a) for v4 in v3]
v5 = []
v4 = 1
v6 = 0
for v7 in range(v1 + 1):
    v8 = v3[v4 - 1]
    if v8 in v5:
        v9 = v5.index(v8)
        break
    v6 += 1
    v5.append(v8)
    v4 = v8
v10 = v5[v9:v6]
if v2 <= v1:
    print(v5[v2 - 1])
else:
    v11 = v2 - v9 - 1
    v12 = v11 % (v6 - v9)
    print(v10[v12])

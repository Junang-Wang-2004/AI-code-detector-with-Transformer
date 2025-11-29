v1, v2, v3 = map(int, input().split())
v4 = input().split()
v5 = input().split()
v6 = []
for v7 in range(len(v4)):
    v6.append(int(v4[v7]))
v8 = []
for v7 in range(len(v5)):
    v8.append(int(v5[v7]))
v9 = []
for v7 in range(v3):
    v10, v11, v12 = map(int, input().split())
    v9.append(v6[v10 - 1] + v8[v11 - 1] - v12)
v9.append(min(v6) + min(v8))
print(min(v9))

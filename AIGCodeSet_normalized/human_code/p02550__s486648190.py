v1, v2, v3 = map(int, input().split())
v4 = [v2]
v5 = set(v4)
v6 = 0
for v7 in range(v1):
    v8 = v4[-1] ** 2 % v3
    if v8 in v5:
        v6 = v4.index(v8)
        break
    else:
        v4.append(v8)
        v5.add(v8)
v9 = v6
v10 = len(v4) - v6
if v10 > 0:
    v11 = sum(v4[:v6]) + sum(v4[v6:]) * ((v1 - v9) // v10) + sum(v4[v6:v6 + (v1 - v9) % v10])
else:
    v11 = sum(v4)
print(v11)

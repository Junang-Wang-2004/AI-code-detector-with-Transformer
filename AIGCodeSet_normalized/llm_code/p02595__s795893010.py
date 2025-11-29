v1, v2 = input().split()
v1 = int(v1)
v2 = int(v2)
v3 = [map(int, input().split()) for v4 in range(v1)]
v5, v6 = [list(i) for v7 in zip(*v3)]
v8 = 0
for v7 in range(v1):
    if (v5[v7] ** 2 + v6[v7] ** 2) ** 0.5 <= v2:
        v8 += 1
    else:
        continue
print(v8)

v1, *v2 = map(int, open(0).read().split())
v3 = min(v2)
v4 = []
for v5 in range(1, v1):
    v4.append((0, v5))
for v5 in range(1, v1):
    v4.append((v5, v5 - 1))
for v5 in range(1, v1):
    v4.append((v5, 0))
print(len(v4))
for v6, v7 in v4:
    print(v6 + 1, v7 + 1)

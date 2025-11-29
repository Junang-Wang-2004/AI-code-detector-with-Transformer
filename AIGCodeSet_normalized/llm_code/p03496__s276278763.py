v1 = int(input())
v2 = list(map(int, input().split()))
v3, v4 = (0, -1)
for v5, v6 in enumerate(v2, start=1):
    if abs(v3) <= abs(v6):
        v3 = v6
        v4 = v5
v7 = [(v4, v5) for v5 in range(1, v1 + 1)]
if v3 >= 0:
    for v5 in range(v1 - 1):
        if v2[v5] > v2[v5 + 1]:
            v7.append((v5 + 1, v5 + 2))
else:
    for v5 in range(v1 - 1, 0, -1):
        if v2[v5 - 1] > v2[v5]:
            v7.append((v5 + 1, v5))
print(len(v7))
for v8, v9 in v7:
    print(v8, v9)

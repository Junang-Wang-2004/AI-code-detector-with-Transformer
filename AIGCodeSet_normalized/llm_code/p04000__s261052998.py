v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v3)]
v4.sort()
v6 = [0]
for v5 in range(1, v3):
    if v4[v5][0] != v4[v5 - 1][0]:
        v6.append(v5)
v6.append(v3)
v4 = [v4[v6[v5]:v6[v5 + 1]] for v5 in range(len(v6) - 1)]
if v3 == 0:
    v4 = []
v7 = [0 for v5 in range(1, 10)]
for v5 in range(len(v4)):
    for v8 in range(len(v4[v5])):
        v7[v4[v5][v8]] += 1
print(*v7)

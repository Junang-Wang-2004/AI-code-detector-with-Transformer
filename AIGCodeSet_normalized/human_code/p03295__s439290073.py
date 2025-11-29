v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v3.sort(key=lambda x: x[1])
v5, v6 = (0, -1)
for v4 in range(v2):
    if v6 < v3[v4][0]:
        v6 = v3[v4][1] - 1
        v5 += 1
print(v5)

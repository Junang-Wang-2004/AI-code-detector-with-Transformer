v1, v2 = map(int, input().split())
v3 = [0] * 1002
for v4 in range(1, 1002):
    v3[v4] = v3[v4 - 1] + v4
    if v3[v4 - 1] - v1 == v3[v4] - v2:
        print(v3[v4 - 1] - v1)
        break

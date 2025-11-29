v1, v2 = map(int, input().split())
v3 = 2 ** (v1 + 1)
if v2 >= v3 // 2 or (v1 == 1 and v2 == 1):
    print(-1)
else:
    v4 = [0] * v3
    for v5 in range(2 ** v1):
        if v5 == v2:
            continue
        v4[v5] = v5
        v4[v3 - 1 - v5] = v5
    v4[v3 // 2 - 1] = v2
    v4[-1] = v2
print(*v4)

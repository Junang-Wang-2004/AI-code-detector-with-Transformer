v1, v2, v3 = map(int, input().split())
v4 = []
v5 = 0
for v6 in range(v1):
    v4.append(list(map(int, input().split())))
v4.sort()
v6 = 0
while v4[-1][1] > 0:
    if v4[v6][1] > 0:
        v7 = v6
        v8 = -(-v4[v6][1] // v3) * v3
        v5 += -(-v4[v6][1] // v3)
        while v4[v7][0] <= v4[v6][0] + 2 * v2:
            v4[v7][1] -= v8
            v7 += 1
            if v7 == v1:
                break
        v4[v6][1] = 0
    v6 += 1
print(v5)

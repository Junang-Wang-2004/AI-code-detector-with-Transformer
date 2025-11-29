v1 = int(input())
v2 = [0] * 1000001
v3 = [0] * 1000000
v2[1] = v1
v4 = 0
for v5 in range(2, 1000001):
    if v2[v5 - 1] % 2 == 0:
        v2[v5] = v2[v5 - 1] // 2
        if v3[v2[v5]] == 0:
            v3[v2[v5]] += 1
        else:
            v4 = v5
            break
    else:
        v2[v5] = 3 * v2[v5 - 1] + 1
        if v3[v2[v5]] == 0:
            v3[v2[v5]] += 1
        else:
            v4 = v5
            break
print(v4)

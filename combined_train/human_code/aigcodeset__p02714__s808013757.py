v1 = int(input())
v2 = input()
v3 = [0, 0, 0]
for v4 in v2:
    if v4 == 'R':
        v3[0] += 1
    elif v4 == 'G':
        v3[1] += 1
    else:
        v3[2] += 1
v5 = v3[0] * v3[1] * v3[2]
for v6 in range(v1):
    for v7 in range(v1):
        v8 = v7 + v6
        v9 = v7 + 2 * v6
        if v8 >= v1 or v9 >= v1:
            break
        if v2[v7] != v2[v8] and v2[v8] != v2[v9] and (v2[v7] != v2[v9]):
            v5 -= 1
print(v5)

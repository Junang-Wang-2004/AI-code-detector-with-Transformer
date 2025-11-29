v1 = int(input())
v2 = input()
v3 = 0
v4 = v1 - 1
v5 = 0
for v6 in range(v1):
    for v7 in range(v1):
        if v2[v7] == 'W':
            v4 = v7
            break
    for v7 in range(v1):
        if v2[v1 - 1 - v7] == 'R':
            v5 = v1 - 1 - v7
            break
    if v4 < v5:
        v2 = v2[:v4] + 'R' + v2[v4 + 1:v5] + 'W' + v2[v5 + 1:]
        v3 += 1
    else:
        break
print(v3)

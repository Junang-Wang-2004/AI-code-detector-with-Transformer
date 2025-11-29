def f1(a1):
    v1 = len(a1)
    v2 = [[0, 0] for v3 in range(v1 + 1)]
    for v4 in range(v1):
        if a1[v4] == 'D':
            v2[v4 + 1][0] = v2[v4][0] + 1
            v2[v4 + 1][1] = v2[v4][1]
        elif a1[v4] == 'P':
            v2[v4 + 1][0] = v2[v4][0]
            if v4 > 0 and a1[v4 - 1] == 'D':
                v2[v4 + 1][1] = v2[v4][1] + 1
            else:
                v2[v4 + 1][1] = v2[v4][1]
        else:
            v2[v4 + 1][0] = max(v2[v4][0] + 1, v2[v4][0])
            if v4 > 0 and a1[v4 - 1] == 'D':
                v2[v4 + 1][1] = max(v2[v4][1] + 1, v2[v4][1])
            else:
                v2[v4 + 1][1] = max(v2[v4][1], v2[v4][1])
    v5 = []
    v4 = v1
    while v4 > 0:
        if a1[v4 - 1] == '?':
            if v2[v4][0] > v2[v4 - 1][0]:
                v5.append('D')
            else:
                v5.append('P')
            v4 -= 1
        else:
            v5.append(a1[v4 - 1])
            v4 -= 1
    return ''.join(v5[::-1])
v1 = input()
print(f1(v1))

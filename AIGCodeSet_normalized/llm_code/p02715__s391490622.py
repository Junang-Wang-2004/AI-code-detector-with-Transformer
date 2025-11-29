v1 = int(input())
v2 = list(map(int, input().split()))
if v1 % 2 == 0:
    v3 = sum(v2[::2])
    print(max(sum(v2) - v3, v3))
elif v1 == 3:
    print(v2[0] + v2[2])
else:
    v4 = -10 ** 12
    v5 = [[v4 for v6 in range(3)] for v7 in range(v1)]
    v5[0][0] = v2[0]
    v5[1][1] = v2[1]
    v5[2][2] = v2[2]
    v5[2][0] = v2[0] + v2[2]
    for v6 in range(3, v1):
        v5[v6][0] = v5[v6 - 2][0] + v2[v6]
        v5[v6][1] = max(v5[v6 - 3][0] + v2[v6], v5[v6 - 2][1] + v2[v6])
        if v6 >= 4:
            v5[v6][2] = max([v5[v6 - 3][1] + v2[v6], v5[v6 - 4][0] + v2[v6], v5[v6 - 2][2] + v2[v6]])
        else:
            v5[v6][2] = max([v5[v6 - 3][1] + v2[v6], v5[v6 - 2][2] + v2[v6]])
    print(max(v5[-1][2], v5[-2][1], v5[-3][0]))

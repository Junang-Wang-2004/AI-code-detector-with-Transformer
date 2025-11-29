v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v2.sort()
v4 = {}
if v1 == 1:
    print(1)
else:
    for v3 in range(v1 - 1):
        for v5 in range(v3 + 1, v1):
            if str(v2[v5][0] - v2[v3][0]) + ' ' + str(v2[v5][1] - v2[v3][1]) in v4:
                v4[str(v2[v5][0] - v2[v3][0]) + ' ' + str(v2[v5][1] - v2[v3][1])] += 1
            else:
                v4[str(v2[v5][0] - v2[v3][0]) + ' ' + str(v2[v5][1] - v2[v3][1])] = 1
    print(v1 - max(v4.values()))

v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[:]
v4 = list(map(int, input().split()))
v5 = v4[:]
v6 = 0
for v7 in range(v1):
    if v7 != v1 - 1:
        if v3[v7] > v4[v7]:
            v3[v7] = v2[v7] - v4[v7]
            v5[v7] = 0
            v6 += v4[v7]
        else:
            v3[v7] = 0
            v5[v7] = v4[v7] - v2[v7]
            v6 += v2[v7]
            if v4[v7] - v2[v7] > 0:
                v3[v7 + 1] = max(v2[v7 + 1] - v5[v7], 0)
                if v5[v7] > v2[v7 + 1]:
                    v6 += v2[v7 + 1]
                else:
                    v6 += v5[v7]
                v5[v7] = 0
    elif v3[v1 - 1] > v4[v1 - 1]:
        v3[v1 - 1] = v2[v1 - 1] - v4[v1 - 1]
        v5[v1 - 1] = 0
        v6 += v4[v7]
    else:
        v3[v1 - 1] = 0
        v5[v1 - 1] = v4[v1 - 1] - v2[v1 - 1]
        v6 += v2[v1 - 1]
        if v4[v1 - 1] - v2[v1 - 1] > 0:
            v3[v1] = max(v2[v1] - v5[v1 - 1], 0)
            if v5[v1 - 1] > v2[v1]:
                v6 += v2[v1]
            else:
                v6 += v5[v1 - 1]
            v5[v1 - 1] = 0
print(v6)

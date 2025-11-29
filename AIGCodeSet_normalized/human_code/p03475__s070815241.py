v1 = int(input())
v2 = []
v1 -= 1
for v3 in range(v1):
    v4, v5, v6 = map(int, input().split())
    v2.append([v4, v5, v6])
for v3 in range(v1 + 1):
    v7 = 0
    for v8 in range(v3, v1):
        if v8 == v3:
            v7 += v2[v8][1] + v2[v8][0]
        elif v7 >= v2[v8][1]:
            v9 = v7 % v2[v8][2]
            v7 += v2[v8][0] + (v2[v8][2] - v9 if v9 != 0 else 0)
        else:
            v7 = v2[v8][1] + v2[v8][0]
    print(v7)

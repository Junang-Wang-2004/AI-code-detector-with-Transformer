v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [0] * v1
v5 = 0
for v6 in range(v1 - 1):
    if v2[v6] > v2[v6 + 1]:
        print(-1)
        exit()
    elif v2[v6] < v2[v6 + 1]:
        v7 = v2[v6 + 1] - v2[v6]
        v4[v6 + 1] = v4[v6] + v7
        v5 += v7
    elif v2[v6] == v2[v6 + 1]:
        v4[v6 + 1] = v4[v6]
if v4 == v2:
    print(v5)
else:
    print(-1)

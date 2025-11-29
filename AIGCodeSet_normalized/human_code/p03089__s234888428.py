v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v5 = -1
    for v6 in range(v1 - v4):
        if v6 + 1 - v2[v6] == 0:
            v5 = v6
    if v5 == -1:
        print(-1)
        exit()
    else:
        v3.append(v2[v5])
        del v2[v5]
[print(a) for v7 in v3[::-1]]

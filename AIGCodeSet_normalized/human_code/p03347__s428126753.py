v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [0] * v1
v5 = 0
v6 = 0
for v3, v7 in enumerate(v2):
    if v7 == 0:
        continue
    if v6 + 1 < v7:
        print(-1)
        exit()
    if v3 - v7 < v5:
        print(-1)
        exit()
    else:
        v4[v3 - v7] = v7
        v5 = v3 - v7
    v6 = v7
print(sum(v4))

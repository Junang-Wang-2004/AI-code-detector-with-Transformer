v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 1
v5 = [-1] * v1
for v6 in range(v2):
    if v5[v4 - 1] == -1:
        v5[v4 - 1] = v6
        v4 = v3[v4 - 1]
    else:
        v7 = v6 - v5[v4 - 1]
        v8 = (v2 - (v6 - v7)) % v7
        v9 = v5.index(v6 - v7 + v8) + 1
        print(v9)
        exit()
print(v4)

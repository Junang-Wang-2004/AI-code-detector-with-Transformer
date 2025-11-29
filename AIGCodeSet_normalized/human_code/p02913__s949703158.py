v1 = int(input())
v2 = input()
v3 = [[0 for v4 in range(v1)] for v4 in range(v1)]
v5 = 0
for v4 in range(v1 - 1):
    for v6 in range(v4 + 1, v1):
        if v3[v4][v6] == 0:
            v7 = 0
            for v8 in range(min(v6 - v4, v1 - 1 - v6 + 1)):
                if v2[v4 + v8] == v2[v6 + v8]:
                    v7 += 1
                else:
                    break
            for v8 in range(1, v7):
                v3[v4 + v8][v6 + v8] = v7 - v8
        v5 = max(v5, v7)
print(v5)

v1, v2 = list(map(int, input().split()))
v3 = [[] for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = list(map(int, input().split()))
    v3[v5 - 1].append((v6, v4))
v7 = [0 for v4 in range(v2)]
for v4 in range(v1):
    v3[v4].sort()
    for v8 in range(len(v3[v4])):
        v9 = '0' * (6 - len(str(v4 + 1))) + str(v4 + 1) + '0' * (6 - len(str(v8 + 1))) + str(v8 + 1)
        v7[v3[v4][v8][1]] = v9
for v4 in range(v2):
    print(v7[v4])

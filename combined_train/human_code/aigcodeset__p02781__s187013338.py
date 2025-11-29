v1 = input()
v2 = len(v1)
v3 = int(input())
v4 = [[[0 for v5 in range(2)] for v5 in range(v3 + 1)] for v5 in range(v2 + 1)]
v4[0][0][0] = 1
for v6 in range(v2):
    for v7 in range(v3 + 1):
        for v8 in range(2):
            v9 = int(v1[v6])
            for v10 in range(10):
                v11, v12, v13 = (v6 + 1, v7, v8)
                if 0 != v10:
                    v12 += 1
                if v12 > v3:
                    continue
                if v13 == 0:
                    if v10 > v9:
                        continue
                    if v10 < v9:
                        v13 = 1
                v4[v11][v12][v13] += v4[v6][v7][v8]
print(sum(v4[-1][-1]))

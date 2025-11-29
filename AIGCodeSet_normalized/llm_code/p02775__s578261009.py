v1 = int(input())
v2 = input()
v3 = len(v2)
v4 = float('inf')
v5 = [[v4] * 2 for v6 in range(v3 + 1)]
v5[0][0] = 0
v5[0][1] = 1
for v7 in range(v3):
    v8 = int(v2[v7])
    v9 = v5[v7][0]
    v10 = v5[v7][1]
    v5[v7 + 1][0] = min(v9 + v8, v10 + min(10 - v8, v8 + 1))
    v5[v7 + 1][1] = min(v9 + v8 + 1, v10 + 10 - v8 - 1)
print(v5[-1][0])

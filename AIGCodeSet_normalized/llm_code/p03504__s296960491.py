v1, v2 = map(int, input().split(' '))
v3 = (10 ** 5 + 2) * 2
v4 = [0 for v5 in range(v3)]
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split(' '))
    v4[v6 * 2 - 1] += 1
    v4[v7 * 2] -= 1
v9 = 0
for v10 in range(1, v3):
    v4[v10] += v4[v10 - 1]
    v9 = max(v9, v4[v10])
print(v9)

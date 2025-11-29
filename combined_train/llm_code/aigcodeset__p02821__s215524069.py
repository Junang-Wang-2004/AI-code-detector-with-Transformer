v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort(reverse=True)
v4 = [0] * (v1 + 1)
for v5 in range(1, v1 + 1):
    v4[v5] = v4[v5 - 1] + v3[v5 - 1]
v6 = [0] * (10 ** 5 + 1)
for v5 in range(v1):
    v6[v3[v5]] += 1
for v5 in range(len(v6) - 1, 0, -1):
    v6[v5 - 1] += v6[v5]
v7 = -1
v8 = 10 ** 5 + 1
while v8 - v7 > 1:
    v9 = (v7 + v8) // 2
    v10 = 0
    for v5 in range(v1):
        v10 += v6[max(1, v9 - v3[v5])]
    if v10 >= v2:
        v7 = v9
    else:
        v8 = v9
v11 = 0
v10 = 0
for v5 in range(v1):
    v12 = max(0, v8 - v3[v5])
    v13 = min(v6[v12], v2 - v10)
    v11 += v4[v13] + v13 * v3[v5]
    v10 += v13
v11 += v7 * (v2 - v10)
print(v11)

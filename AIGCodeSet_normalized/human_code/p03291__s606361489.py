v1 = input()
v2 = len(v1)
v3 = 10 ** 9 + 7
v4 = [0] * v2
v5 = [0] * v2
v6 = [0] * v2
v7 = [0] * v2
for v8 in range(v2 - 1):
    v9 = v1[v8]
    if v9 == 'A':
        v4[v8 + 1] = v4[v8] + 1
    else:
        v4[v8 + 1] = v4[v8]
    if v9 == '?':
        v6[v8 + 1] = v6[v8] + 1
    else:
        v6[v8 + 1] = v6[v8]
for v8 in range(v2 - 1, 0, -1):
    v9 = v1[v8]
    if v9 == 'C':
        v5[v8 - 1] = v5[v8] + 1
    else:
        v5[v8 - 1] = v5[v8]
    if v9 == '?':
        v7[v8 - 1] = v7[v8] + 1
    else:
        v7[v8 - 1] = v7[v8]
v10 = 0
for v8 in range(v2):
    if v1[v8] == 'B' or v1[v8] == '?':
        v10 = (v10 + (v4[v8] * pow(3, v6[v8], v3) + v6[v8] * pow(3, max(0, v6[v8] - 1), v3)) * (v5[v8] * pow(3, v7[v8], v3) + v7[v8] * pow(3, max(0, v7[v8] - 1), v3))) % v3
print(v10)

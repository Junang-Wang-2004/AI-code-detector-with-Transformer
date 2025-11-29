v1 = int(input())
v2 = [input() for v3 in range(v1)]
v4 = [0] * v1
v5 = [0] * v1
for v6 in range(v1):
    if v2[v6][-1] == 'A':
        v4[v6] = 1
    if v2[v6][0] == 'B':
        v5[v6] = 1
v7 = sum((a * b for v8, v9 in zip(v4, v5)))
for v6 in range(v1):
    if v4[v6] == 1 and v5[v6] == 1:
        v7 -= 1
        break
print(v7)

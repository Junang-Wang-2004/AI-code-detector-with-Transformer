v1 = input()
v2 = 10 ** 9 + 7
v3 = 0
v4 = len(v1)
v5 = [0] * (v4 + 1)
for v6 in range(1, v4 + 1):
    if v1[v6 - 1] == '1':
        v5[v6] = v5[v6 - 1] + 1
    else:
        v5[v6] = v5[v6 - 1]
v3 += pow(2, v5[v4], v2)
for v7 in range(0, v4):
    if v1[v7] == '0':
        continue
    v3 += pow(2, v5[v7], v2) * pow(3, v4 - 1 - v7, v2)
print(v3 % v2)

v1 = int(input())
v2 = 10 ** 9 + 7
v3 = [0] * (v1 + 1)
v3[0] = 1
v3[1] = 4
v3[2] = 16
for v4 in range(3, v1 + 1):
    v3[v4] = (4 * v3[v4 - 1] - v3[v4 - 3]) % v2
print(v3[v1])

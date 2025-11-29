v1 = int(input())
v2 = 9
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v4 = 0
while v2 < v1:
    if v3[v4] % 10 != 0:
        v3.append(v3[v4] * 10 + v3[v4] % 10 - 1)
        v2 = v2 + 1
    v3.append(v3[v4] * 10 + v3[v4] % 10)
    v2 = v2 + 1
    if v3[v4] % 10 != 9:
        v3.append(v3[v4] * 10 + v3[v4] % 10 + 1)
        v2 = v2 + 1
    v4 = v4 + 1
print(v3[v1 - 1])

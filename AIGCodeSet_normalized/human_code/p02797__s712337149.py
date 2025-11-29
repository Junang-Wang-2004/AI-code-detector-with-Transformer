v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v2):
    v4.append(v3)
for v5 in range(v1 - v2):
    if v3 != 10 ** 9:
        v4.append(10 ** 9)
    else:
        v4.append(10 ** 9 - 1)
v6 = ''
for v5 in v4:
    v6 += str(v5) + ' '
print(v6)

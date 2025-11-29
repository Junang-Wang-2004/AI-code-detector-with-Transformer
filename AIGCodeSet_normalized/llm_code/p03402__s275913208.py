v1, v2 = map(int, input().split())
v3 = 50
v4 = []
for v5 in range(2 * v3):
    v4.append(['#'] * (2 * v3))
v1, v2 = (v1 - 1, v2 - 1)
for v5 in range(0, 2 * v3, 2):
    for v6 in range(0, 2 * v3, 2):
        if v1 > 0:
            v4[v5][v6] = '.'
            v1 -= 1
for v5 in range(1, 2 * v3, 2):
    for v6 in range(1, 2 * v3, 2):
        if v2 > 0:
            v4[v5][v6] = '#'
            v2 -= 1
print(2 * v3, 2 * v3)
for v5 in v4:
    print(''.join(v5))

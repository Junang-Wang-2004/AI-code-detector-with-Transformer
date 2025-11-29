def f1(a1, a2):
    v1, v2 = (2 * a1 + 1, 2 * a2 + 1)
    v3 = [['.' for v4 in range(v2)] for v4 in range(v1)]
    for v5 in range(a1):
        v3[2 * v5][0] = '#'
    for v5 in range(a2):
        v3[0][2 * v5] = '#'
    for v5 in range(1, v1):
        for v6 in range(1, v2):
            if v5 % 2 == 0 and v6 % 2 == 0:
                v3[v5][v6] = '#'
    for v7 in v3:
        print(''.join(v7))
v1, v2 = map(int, input().split())
print(2 * v1 + 1, 2 * v2 + 1)
f1(v1, v2)

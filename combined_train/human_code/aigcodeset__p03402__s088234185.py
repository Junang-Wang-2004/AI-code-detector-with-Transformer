v1, v2 = map(int, input().split())
v3 = [['#' for v4 in range(100)] for v5 in range(50)] + [['.' for v4 in range(100)] for v5 in range(50)]
print(100, 100)
v1 -= 1
for v4 in range(1, 49):
    for v5 in range(1, 99):
        if all([v3[v4 + x][v5 + y] == '#' for v6, v7 in ((0, 0), (0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))]):
            if v1 == 0:
                break
            v3[v4][v5] = '.'
            v1 -= 1
    if v1 == 0:
        break
v2 -= 1
for v4 in range(51, 99):
    for v5 in range(1, 99):
        if all([v3[v4 + v6][v5 + v7] == '.' for v6, v7 in ((0, 0), (0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))]):
            if v2 == 0:
                break
            v3[v4][v5] = '#'
            v2 -= 1
    if v2 == 0:
        break
for v4 in v3:
    print(''.join(v4))

v1, v2 = map(int, input().split())
v3 = [['.' for v4 in range(3)] for v5 in range(3)]
v6 = [['#' for v4 in range(3)] for v5 in range(3)]
v7 = [['#' for v4 in range(3)] for v5 in range(3)]
v8 = [['.' for v4 in range(3)] for v5 in range(3)]
v7[1][1] = '.'
v8[1][1] = '#'
v9 = [['.' for v4 in range(99)] for v5 in range(96)]
v1 -= 1
v2 -= 1
v10 = v1 // 33
v11 = v1 % 33
for v4 in range(17):
    for v5 in range(33):
        if v10 > v4:
            for v12 in range(3):
                for v13 in range(3):
                    v9[v4 * 3 + v12][v5 * 3 + v13] = v7[v12][v13]
        elif v10 == v4:
            if v11 > v5:
                for v12 in range(3):
                    for v13 in range(3):
                        v9[v4 * 3 + v12][v5 * 3 + v13] = v7[v12][v13]
            else:
                for v12 in range(3):
                    for v13 in range(3):
                        v9[v4 * 3 + v12][v5 * 3 + v13] = v3[v12][v13]
        else:
            for v12 in range(3):
                for v13 in range(3):
                    v9[v4 * 3 + v12][v5 * 3 + v13] = v3[v12][v13]
if v1 > 0 and v10 < 15:
    v2 -= 1
if v2 == -1:
    print(51, 99)
    for v4 in range(48):
        print(*v9[v4], sep='')
    exit()
v14 = v2 // 33
v15 = v2 % 33
for v4 in range(17, 17 + 16, 1):
    for v5 in range(33):
        if v14 > v4 - 17:
            for v12 in range(3):
                for v13 in range(3):
                    v9[v4 * 3 + v12][v5 * 3 + v13] = v8[v12][v13]
        elif v14 == v4 - 17:
            if v15 > v5:
                for v12 in range(3):
                    for v13 in range(3):
                        v9[v4 * 3 + v12][v5 * 3 + v13] = v8[v12][v13]
            else:
                for v12 in range(3):
                    for v13 in range(3):
                        v9[v4 * 3 + v12][v5 * 3 + v13] = v6[v12][v13]
        else:
            for v12 in range(3):
                for v13 in range(3):
                    v9[v4 * 3 + v12][v5 * 3 + v13] = v6[v12][v13]
print(99, 99)
for v4 in range(99):
    print(*v9[v4], sep='')

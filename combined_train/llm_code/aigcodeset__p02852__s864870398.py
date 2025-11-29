def f1():
    v1, v2 = inpm()
    v3 = input()
    v4 = [0] * (v1 + 1)
    v4[0] = 0
    for v5 in range(1, v1 + 1):
        for v6 in range(max(0, v5 - v2), v5):
            if v4[v6] == -1:
                continue
            v7 = v5 - v6
            v8 = int(v4[v6] + str(v7))
            v8 = str(v8)
            if v4[v5] == 0:
                v4[v5] = v8
            elif len(v4[v5]) == len(v8):
                v4[v5] = str(max(int(v4[v5]), int(v8)))
            elif len(v4[v5]) > len(v8):
                v4[v5] = v8
            elif len(v4[v5]) < len(v8):
                continue
    if int(v4[v1]) == 0:
        print(-1)
    else:
        v9 = list(v4[v1])
        v9.reverse()
        print(' '.join(v9))

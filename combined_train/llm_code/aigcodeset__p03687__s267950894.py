def f1():
    v1 = input()
    v2 = {}
    v3 = ''
    v4 = 0
    v5 = ''
    for v6 in v1:
        v2[v6] = 0
    for v6 in v1:
        v2[v6] += 1
    for v6 in v1:
        v4 = max(v4, v2[v6])
    for v6 in v1:
        if v2[v6] == v4:
            v3 += v6
    if v4 == 1:
        v5 = v1[int(len(v1) / 2)]
    for v6 in v1[int((len(v1) + v4 - 1) / v4):]:
        if v6 in v3:
            v5 = v6
            break
    v7 = {}
    v8 = 0
    while True:
        if len({v6 for v6 in v1}) == 1:
            break
        else:
            for v6, v9 in enumerate(v1):
                if v9 == v5:
                    v10 = list(v1)
                    if v6 > 0:
                        v10[v6 - 1] = v5
                    v1 = ''.join(v10)
            v1 = v1[:len(v1) - 1]
            v8 += 1
        if v8 == 10:
            break
    print(v8)
if __name__ == '__main__':
    f1()

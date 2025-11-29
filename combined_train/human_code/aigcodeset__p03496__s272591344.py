def f1():
    v1, *v2 = map(int, open(0).read().split())
    v3, v4 = (min(v2), max(v2))
    if v3 == v4:
        print(0)
        exit()
    v5 = []
    v6, v7 = (v2.index(v3) + 1, v2.index(v4) + 1)
    if abs(v3) > abs(v4):
        for v8 in range(v1):
            if v2[v8] > 0:
                v5.append((v6, v8 + 1))
        for v8 in range(v1 - 1):
            v5.append((v1 - v8, v1 - v8 - 1))
    else:
        for v8 in range(v1):
            if v2[v8] < 0:
                v5.append((v7, v8 + 1))
        for v8 in range(v1 - 1):
            v5.append((v8 + 1, v8 + 2))
    print(len(v5))
    print('\n'.join(['{} {}'.format(v8[0], v8[1]) for v8 in v5]))
if __name__ == '__main__':
    f1()

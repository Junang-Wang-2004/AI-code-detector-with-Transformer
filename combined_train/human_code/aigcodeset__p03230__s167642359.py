def f1():
    v1 = int(input())
    if v1 == 1:
        v2 = ['Yes', '2', '1 1', '1 1']
        return print(*v2, sep='\n')
    if v1 == 2:
        return print('No')
    v3 = -1
    for v4 in range(2, int((2 * v1) ** 0.5) + 2):
        if 2 * v1 % v4 > 0:
            continue
        if 2 * v1 // v4 == v4 - 1:
            v3 = v4
            break
    if v3 == -1:
        return print('No')
    v5 = v3 - 1
    v6 = [[v5] for v7 in range(v3)]
    for v4 in range(v5):
        v8 = v5 * (v5 + 1) // 2 - (v5 - v4) * (v5 - v4 + 1) // 2 + 1
        v9 = [x for v10 in range(v8, v8 + v5 - v4)]
        v6[v4] += v9
        for v11 in range(v5 - v4):
            v6[v4 + 1 + v11].append(v9[v11])
    print('Yes')
    print(v3)
    for v12 in v6:
        print(*v12, sep=' ')
if __name__ == '__main__':
    f1()

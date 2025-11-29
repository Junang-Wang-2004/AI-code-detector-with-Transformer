def f1():
    v1 = int(input())
    v2 = int((2 * v1) ** 0.5)
    if 2 * v1 != v2 * (v2 + 1):
        print('No')
    else:
        print('Yes')
        print(v2 + 1)
        v3 = []
        v4 = 1
        for v5 in range(v2):
            v6 = [v2]
            v6.extend(list(range(v4, v4 + v5 + 1)))
            v7 = v6[-1]
            for v8 in range(v5 + 1, v2):
                v7 += v8
                v6.append(v7)
            v3.append(' '.join([str(_) for v9 in v6]))
            v4 += v5 + 1
        v6 = [v2]
        v4 = 0
        for v5 in range(0, v2):
            v4 += v5 + 1
            v6.append(v4)
        v3.append(' '.join([str(v9) for v9 in v6]))
        print('\n'.join(v3))
f1()

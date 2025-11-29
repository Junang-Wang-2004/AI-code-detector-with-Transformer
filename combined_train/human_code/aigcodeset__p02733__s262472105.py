v1 = 'E'
if v1 == 'A':
    v2, v3 = map(int, input().split())
    v4 = 0
    v4 += v3 * (v3 - 1) // 2
    v4 += v2 * (v2 - 1) // 2
    print(v4)
if v1 == 'B':

    def f1(a1):
        for v1 in range(len(a1) // 2 + 1):
            if a1[v1] != a1[-(v1 + 1)]:
                return False
        return True
    v5 = input()
    v2 = len(v5)
    if f1(v5) and f1(v5[:(v2 - 1) // 2]) and f1(v5[(v2 + 3) // 2 - 1:]):
        print('Yes')
    else:
        print('No')
if v1 == 'C':
    v6 = int(input())
    print(v6 ** 3 / 27)
if v1 == 'D':
    v2 = int(input())
    v7 = [int(i) for v8 in input().split()]
    v9 = list(set(v7))
    v10 = {}
    for v11 in v9:
        v10[v11] = 0
    for v12 in v7:
        v10[v12] += 1
    v13 = 0
    for v11 in v9:
        v13 += v10[v11] * (v10[v11] - 1) // 2
    for v12 in v7:
        if v10[v12] >= 2:
            print(v13 - v10[v12] + 1)
        else:
            print(v13)
if v1 == 'E':

    def f2(a1, a2):
        return [v12 + b for v12, v1 in zip(a1, a2)]

    def f3(a1, a2, a3):
        v1 = 0
        if max(max(a1)) > a2:
            return -1
        v2 = a1[0]
        for v3 in range(1, a3):
            v2 = f2(v2, a1[v3])
            if max(v2) > a2:
                v1 += 1
                v2 = a1[v3]
        return v1
    v14, v15, v11 = map(int, input().split())
    v16 = [[int(v8) for v8 in input()] for v17 in range(v14)]
    v4 = v14 * v15
    for v8 in range(2 ** (v14 - 1)):
        v18 = []
        v19 = v16[0]
        v20 = bin(v8 + 2 ** v14)[4:]
        for v17 in range(1, v14):
            if v20[v17 - 1] == '0':
                v19 = f2(v19, v16[v17])
            else:
                v18.append(v19)
                v19 = v16[v17]
        v18.append(v19)
        v21 = f3([list(x) for v22 in zip(*v18)], v11, v15)
        if v21 == -1:
            continue
        v21 += v20.count('1')
        if v4 > v21:
            v4 = v21
    print(v4)

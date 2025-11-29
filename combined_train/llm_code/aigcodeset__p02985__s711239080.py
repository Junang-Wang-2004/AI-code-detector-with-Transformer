import collections

def f1():
    v1, v2 = map(int, input().split())
    if v2 == 1:
        if v1 == 1:
            return 1
        else:
            return 0
    v3 = collections.defaultdict(list)
    for v4 in range(v1 - 1):
        v5, v6 = map(int, input().split())
        v3[v5].append(v6)
        v3[v6].append(v5)
    v7 = pow(10, 9) + 7
    v8 = f4(v2 - 1, v7)
    v9 = [v8]
    for v10 in range(v2 - 1, 0, -1):
        v9.append(v9[-1] * v10 % v7)
    v9 = v9[::-1]
    v11 = [1]
    for v10 in range(1, v2):
        v11.append(v11[-1] * v10 % v7)
    v12 = v2
    v13 = []
    v14 = set([1])
    for v6 in v3[1]:
        v13.append(v6)
        v14.add(v6)
    v15 = len(v13)
    if v15 > v2 - 1:
        return 0
    v12 *= v11[v2 - 1] * v9[v2 - 1 - v15] % v7
    v12 %= v7
    while v13:
        v16 = []
        for v5 in v13:
            v15 = len(v3[v5]) - 1
            for v6 in v3[v5]:
                if v6 not in v14:
                    v15 -= 1
            if v15 > v2 - 2:
                return 0
            v12 *= v11[v2 - 2] * v9[v2 - 2 - v15] % v7
            v12 %= v7
            for v6 in v3[v5]:
                if v6 not in v14:
                    v16.append(v6)
                    v14.add(v6)
        v13 = v16
    return v12

def f2(a1, a2, a3):
    if a2 == 0:
        return 1
    elif a2 == 1:
        return a1
    elif a2 % 2 == 0:
        return pow(f2(a1, a2 // 2, a3), 2) % a3
    elif a2 % 2 == 1:
        return pow(f2(a1, a2 // 2, a3), 2) * a1 % a3

def f3(a1, a2):
    v1 = 1
    for v2 in range(2, a1 + 1):
        v1 *= v2
        v1 %= a2
    return v1

def f4(a1, a2):
    v1 = f3(a1, a2)
    return f2(v1, a2 - 2, a2)
if __name__ == '__main__':
    print(f1())

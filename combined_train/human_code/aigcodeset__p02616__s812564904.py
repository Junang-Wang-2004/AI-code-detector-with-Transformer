def f1(a1):
    v1 = int(1000000000.0) + 7
    v2 = 1
    for v3 in a1:
        v2 *= v3
        v2 %= v1
    return v2

def f2():
    """
    import random
    limit = int(1e9)
    n = int(2e5)
    k = int(n*9/10)
    x = []
    for i in range(n):
        x.append(random.randint(-limit,limit))
    """
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    if v1 == v2:
        return f1(v3)
    if v3.count(0) > v1 - v2:
        return 0
    v3.append(0)
    v3.sort()
    v4 = v3.index(0)
    v5 = v3.count(0)
    v6 = v3[:v4]
    v7 = v3[v4 + v5:]
    v8 = v3[v4:v4 + v5 - 1]
    if len(v7) == 0:
        if v2 % 2 == 0:
            return f1(v6[:v2])
        elif len(v8) != 0:
            return 0
        else:
            return f1(v6[-v2:])
    v9 = 1
    if v2 % 2 == 1:
        v9 *= v7[-1]
        v7.pop(-1)
        v2 -= 1
    v10, v11 = ([], [])
    for v12 in range(0, 2 * int(len(v6) / 2), 2):
        v10.append(v6[v12] * v6[v12 + 1])
    v7.sort(reverse=True)
    for v12 in range(0, 2 * int(len(v7) / 2), 2):
        v11.append(v7[v12] * v7[v12 + 1])
    v10.extend(v11)
    v10.sort(reverse=True)
    v10.insert(0, v9)
    v13 = int(v2 / 2)
    if len(v10) > v13:
        return f1(v10[:int(v2 / 2) + 1])
    elif len(v8) != 0:
        return 0
    else:
        return -1
print(f2())

v1 = 10 ** 9 + 7

def f1(a1=False):
    v1 = [int(i) for v2 in input().split()]
    if len(v1) == 1 and (not a1):
        return v1[0]
    return v1

def f2(a1):
    v1 = []
    for v2 in range(2, int(a1 ** 0.5) + 1):
        while a1 % v2 == 0:
            a1 //= v2
            v1.append(v2)
        if v2 > a1:
            break
    if a1 != 1:
        v1.append(a1)
    return v1

def f3(a1, a2, a3, a4=False):
    if a1 <= 0:
        return 0
    if a2 == 0:
        return 1
    if a2 < 0:
        return 0
    if a2 == 1:
        return a1
    v1 = 1
    for v2 in range(a1 - a2 + 1, a1 + 1):
        v1 *= v2
        v1 = v1 % a3
    v3 = 1
    for v2 in range(1, a2 + 1):
        v3 *= v2
        v3 = v3 % a3
    v1 = v1 * f4(v3, a3) % a3
    if a4:
        pass
    return v1

def f4(a1, a2):
    return f5(a1, a2 - 2)

def f5(a1, a2):
    if a2 == 0:
        return 1
    if a2 % 2 == 0:
        return f5(a1, a2 // 2) ** 2 % v1
    if a2 % 2 == 1:
        return a1 * f5(a1, a2 - 1) % v1

def f6():
    v1, v2, v3, v4, v5 = f1()
    v6 = f1(listed=True)
    v7 = f1(listed=True)
    v8 = f1(listed=True)
    v6.sort(reverse=True)
    v7.sort(reverse=True)
    v8.sort(reverse=True)
    v9 = v6[:v1]
    v10 = v7[:v2]
    v9.sort()
    v10.sort()
    v11 = 0
    v12 = 0
    for v13 in v8:
        if min(v9[v11], v10[v12]) < v13:
            if v9[v11] < v10[v12]:
                v9[v11] = v13
                v11 += 1
            else:
                v10[v12] = v13
                v12 += 1
        else:
            break
    print(sum(v9) + sum(v10))
    pass
if __name__ == '__main__':
    f6()

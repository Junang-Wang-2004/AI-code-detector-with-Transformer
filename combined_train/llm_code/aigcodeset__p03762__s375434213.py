def f1():
    return [int(e) for v1 in input().split()]

def f2():
    return [s for v1 in input().split()]

def f3(a1, a2):
    v1 = 0
    v2 = max(a1)
    v3 = max(a2)
    v4 = min(a1)
    v5 = min(a2)

    def one_fold(a1, a2=False):
        if len(a1) == 2:
            if a2:
                return [v2 - v4]
            else:
                return [v3 - v5]
        else:
            return [a1[i] - a1[i - 1] for v1 in range(1, len(a1))]
    v6 = one_fold(a1, x=True)
    v7 = one_fold(a2)
    while True:
        if len(v6) == 1 and len(v7) == 1:
            break
        for v8 in v6:
            for v9 in v7:
                v1 += v8 * v9
        if len(v6) > len(v7):
            v6 = one_fold(v6, x=True)
        else:
            v7 = one_fold(v7)
    v1 += v2 * v3
    return v1 % (pow(10, 9) + 7)
if __name__ == '__main__':
    v1, v2 = f1()
    v3 = f1()
    v4 = f1()
    print(f3(v3, v4))

def f1():
    v1 = input()
    v2 = int(input())
    v3 = 0
    v4 = 0
    v5 = v1[0]
    v6 = 0
    for v7 in v1:
        if v5 == v7:
            v3 += 1
            v5 = v7
        else:
            v4 += v3 // 2
            if v6 == 0:
                v6 = v3
            v3 = 1
            v5 = v7
    if v6 == 0:
        v6 = v3
    v4 += v3 // 2
    v4 *= v2
    if len(v1) == v6:
        v4 = len(v1) * v2 // 2
    elif v1[0] == v1[-1] and v3 % 2 == 1 and (v6 % 2 == 1):
        v4 += v2 - 1
    print(v4)
if __name__ == '__main__':
    f1()

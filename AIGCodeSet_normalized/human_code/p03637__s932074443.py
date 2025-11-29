def f1():
    v1 = int(input())
    v2 = [int(i) for v3 in input().split()]
    v4 = 0
    v5 = 0
    for v6 in v2:
        if v6 % 2 == 0:
            if v6 % 4 == 0:
                v5 += 1
            else:
                v4 += 1
    v7 = int(v4 / 2)
    v8 = 3 + (v5 - 1) * 2 + v7 * 2
    if v1 <= v8:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    f1()

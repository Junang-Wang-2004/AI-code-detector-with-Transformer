def f1():
    v1, v2, v3, v4 = list(map(int, input().split()))
    v5 = True
    while v1 > 0 and v3 > 0:
        if v5:
            v3 -= v2
        else:
            v1 -= v4
        v5 = not v5
    if v1 > 0:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    f1()

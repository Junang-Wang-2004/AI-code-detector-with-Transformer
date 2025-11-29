def f1():
    v1 = input()
    v2, v3 = [int(x) for v4 in v1.split()]
    v5 = (4 * v2 - v3) / 2
    v6 = v5 >= 0 and v5 <= v2 and (v5 % 1 == 0)
    if v6:
        print('Yes')
    else:
        print('No')
f1()

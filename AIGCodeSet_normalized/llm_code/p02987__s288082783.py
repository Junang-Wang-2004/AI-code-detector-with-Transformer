def f1():
    v1 = input()
    v1 = sorted(v1)
    if v1[0] == v1[1] and v1[2] == v1[3] and (v1[0] != v1[2]):
        print('Yes')
    else:
        print('No')
f1()

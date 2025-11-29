def f1():
    v1 = int(input())
    if v1 % 2 != 0:
        print(0)
        return
    if v1 <= 8:
        print(0)
        return
    v2 = 0
    v3 = 0
    while True:
        v4 = 10 * 5 ** v3
        if v1 // v4 > 0:
            v2 += v1 // v4
        else:
            break
        v3 += 1
    print(v2)
f1()

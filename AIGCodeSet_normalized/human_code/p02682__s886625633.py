def f1():
    v1, v2, v3, v4 = [int(x) for v5 in input().split()]
    v6 = 0
    if v1 >= v4:
        print(v4)
        return
    v6 += v1
    v4 -= v1
    if v2 >= v4:
        print(v6)
        return
    v4 -= v2
    print(v6 - v4)
if __name__ == '__main__':
    f1()

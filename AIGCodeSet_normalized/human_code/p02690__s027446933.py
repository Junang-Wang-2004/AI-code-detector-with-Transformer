def f1():
    v1 = int(input())
    for v2 in range(-200, 200):
        v3 = v2 ** 5
        for v4 in range(v2 + 1, 200):
            v5 = v4 ** 5
            if v5 - v3 == v1:
                print(v4, v2)
                exit()
f1()

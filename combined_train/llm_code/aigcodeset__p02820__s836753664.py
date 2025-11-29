def f1():
    """
    code here
    """
    v1, v2 = [int(item) for v3 in input().split()]
    v4, v5, v6 = [int(v3) for v3 in input().split()]
    v7 = input()
    v8 = min(v2, v1 - v2)
    v9 = [1 for v10 in range(v8)]

    def point_chk(a1):
        if a1 == 'r':
            return v6
        elif a1 == 's':
            return v4
        elif a1 == 'p':
            return v5
        else:
            raise
    v11 = 0
    for v12, v13 in enumerate(v7):
        if v12 < v2:
            v11 += point_chk(v13)
            v9[v12 % v8] = v13
        elif v13 == v9[v12 % v2]:
            pass
        else:
            v9[v12 % v2] = v13
            v11 += point_chk(v13)
    print(v11)
if __name__ == '__main__':
    f1()

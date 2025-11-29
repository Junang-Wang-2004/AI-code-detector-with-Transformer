v1 = input()

def f1(a1):
    if len(v1) == 1:
        return 0
    else:
        v1 = v1[0]
        v2 = 0
        v3 = 0
        for v4 in range(1, a1):
            if v1[v4] != v1:
                v1 = v1[v4]
                v3 = 0
                v2 += v4 + 1
            else:
                v3 += 1
                v2 += v3
        return v2

def f1():
    from itertools import accumulate
    v1, v2 = (int(i) for v3 in input().split())
    v4 = [int(v3) for v3 in input().split()]
    v5 = sum(v4)

    def enum_divisors(a1):
        v1 = []
        for v2 in range(1, a1 + 1):
            if v2 * v2 > a1:
                break
            if a1 % v2 == 0:
                v1.append(v2)
                if a1 // v2 != v2:
                    v1.append(a1 // v2)
        return v1
    v6 = enum_divisors(v5)
    v6.sort(reverse=True)
    for v7 in v6:
        if v7 == 1:
            print(v7)
            return
        v8 = []
        for v9 in v4:
            if v9 % v7 != 0:
                v8.append(v9 % v7)
        v8.sort()
        v10 = [v7 - dn for v11 in v8]
        v12 = list(accumulate([0] + v8))
        v13 = list(accumulate([0] + v10))
        v14 = len(v12) - 1
        if min((v12[v3] for v3 in range(1, v14) if v12[v3] - (v13[v14] - v13[v3]) == 0)) <= v2:
            print(v7)
            return
if __name__ == '__main__':
    f1()

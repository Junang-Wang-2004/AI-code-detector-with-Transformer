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
        v8 = []
        for v9 in v4:
            v8.append(v9 % v7)
        v8.sort()
        v10 = list(accumulate([0] + v8))
        if min((v10[v3] for v3 in range(1, v1) if v10[v3] == v7 * (v1 - v3) - (v10[v1] - v10[v3]))) <= v2:
            print(v7)
            return
if __name__ == '__main__':
    f1()

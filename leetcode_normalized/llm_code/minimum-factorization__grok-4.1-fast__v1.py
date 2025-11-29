class C1:

    def smallestFactorization(self, a1):
        if a1 < 2:
            return a1
        v1 = []
        for v2 in range(9, 1, -1):
            while a1 % v2 == 0:
                v1.append(v2)
                a1 //= v2
        if a1 != 1:
            return 0
        v1.reverse()
        v4 = ''.join((str(x) for v5 in v1))
        v6 = int(v4)
        return v6 if v6 < 2 ** 31 else 0

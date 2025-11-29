class C1:

    def countPrimes(self, a1):
        if a1 <= 2:
            return 0
        v1 = [True] * a1
        v1[0] = v1[1] = False
        for v2 in range(2, int(a1 ** 0.5) + 1):
            if v1[v2]:
                for v3 in range(v2 * v2, a1, v2):
                    v1[v3] = False
        return sum(v1)

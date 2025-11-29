class C1:

    def distinctPrimeFactors(self, a1):
        v1 = set()
        v2 = set(a1)
        for v3 in v2:
            if v3 < 2:
                continue
            v4 = 2
            while v4 * v4 <= v3:
                while v3 % v4 == 0:
                    v1.add(v4)
                    v3 //= v4
                v4 += 1
            if v3 > 1:
                v1.add(v3)
        return len(v1)

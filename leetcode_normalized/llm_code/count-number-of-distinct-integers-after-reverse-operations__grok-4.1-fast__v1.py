class C1:

    def countDistinctIntegers(self, a1):
        v1 = set()
        for v2 in a1:
            v1.add(v2)
            v3 = v2
            v4 = 0
            while v3 > 0:
                v4 = v4 * 10 + v3 % 10
                v3 //= 10
            v1.add(v4)
        return len(v1)

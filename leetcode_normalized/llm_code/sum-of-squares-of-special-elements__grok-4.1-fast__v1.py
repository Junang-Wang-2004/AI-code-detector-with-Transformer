class C1:

    def sumOfSquares(self, a1):
        v1 = len(a1)
        v2 = set()
        v3 = int(v1 ** 0.5) + 1
        for v4 in range(1, v3):
            if v1 % v4 == 0:
                v2.add(v4)
                v2.add(v1 // v4)
        return sum((a1[d - 1] * a1[d - 1] for v5 in v2))

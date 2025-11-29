class C1(object):

    def sumDigitDifferences(self, a1):
        """
        """
        v1, v2 = (1, 0)
        while v1 <= a1[0]:
            v1 *= 10
            v2 += 1
        v3 = [[0] * 10 for v4 in range(v2)]
        for v5 in a1:
            for v6 in range(v2):
                v3[v6][v5 % 10] += 1
                v5 //= 10
        return sum((c * (len(a1) - c) for v7 in v3 for v8 in v7)) // 2

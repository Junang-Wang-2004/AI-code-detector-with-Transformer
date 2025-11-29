class C1(object):

    def countNumbersWithUniqueDigits(self, a1):
        """
        """
        v1 = [1] * 2

        def nPr(a1, a2):
            while len(v1) <= a1:
                v1.append(v1[-1] * len(v1))
            return v1[a1] // v1[a1 - a2]
        return 1 + 9 * sum((nPr(9, i) for v2 in range(a1)))

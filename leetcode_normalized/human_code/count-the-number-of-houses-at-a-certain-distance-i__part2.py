class C1(object):

    def countOfPairs(self, a1, a2, a3):
        """
        """
        a2, a3 = (a2 - 1, a3 - 1)
        v3 = [0] * a1
        for v4 in range(a1):
            for v5 in range(v4 + 1, a1):
                v3[min(abs(v4 - v5), abs(v4 - a2) + 1 + abs(a3 - v5), abs(v4 - a3) + 1 + abs(a2 - v5)) - 1] += 2
        return v3

class C1(object):

    def splitArraySameAverage(self, a1):
        """
        """

        def possible(a1, a2):
            for v1 in range(1, a2 // 2 + 1):
                if a1 * v1 % a2 == 0:
                    return True
            return False
        v1, v2 = (len(a1), sum(a1))
        if not possible(v1, v2):
            return False
        v3 = [set() for v4 in range(v1 // 2 + 1)]
        v3[0].add(0)
        for v5 in a1:
            for v6 in reversed(range(1, v1 // 2 + 1)):
                for v7 in v3[v6 - 1]:
                    v3[v6].add(v7 + v5)
        for v6 in range(1, v1 // 2 + 1):
            if v2 * v6 % v1 == 0 and v2 * v6 // v1 in v3[v6]:
                return True
        return False

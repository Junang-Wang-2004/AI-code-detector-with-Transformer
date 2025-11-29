class C1(object):

    def sumCounts(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        for v3 in range(len(a1)):
            v4 = set()
            for v5 in reversed(range(v3 + 1)):
                v4.add(a1[v5])
                v2 = (v2 + len(v4) ** 2) % v1
        return v2

class C1(object):

    def countTriples(self, a1):
        """
        """
        v1 = set()
        for v2 in range(1, a1 + 1):
            v1.add(v2 ** 2)
        v3 = 0
        for v2 in range(1, a1 + 1):
            for v4 in range(1, a1 + 1):
                v3 += int(v2 ** 2 + v4 ** 2 in v1)
        return v3

class C1(object):

    def hasSameDigits(self, a1):
        """
        """
        a1 = list(map(int, a1))
        for v2 in reversed(range(3, len(a1) + 1)):
            for v3 in range(v2 - 1):
                a1[v3] = (a1[v3] + a1[v3 + 1]) % 10
        return a1[0] == a1[1]

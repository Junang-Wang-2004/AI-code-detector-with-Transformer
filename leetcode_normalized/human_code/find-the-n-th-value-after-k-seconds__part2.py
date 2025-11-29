class C1(object):

    def valueAfterKSeconds(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [1] * a1
        for v3 in range(a2):
            for v4 in range(1, a1):
                v2[v4] = (v2[v4] + v2[v4 - 1]) % v1
        return v2[-1]

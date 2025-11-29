class C1(object):

    def xorAfterQueries(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        for v2, v3, v4, v5 in a2:
            for v6 in range(v2, v3 + 1, v4):
                a1[v6] = a1[v6] * v5 % v1
        return reduce(lambda accu, x: accu ^ x, a1, 0)

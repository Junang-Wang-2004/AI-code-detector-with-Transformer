class C1(object):

    def fixedRatio(self, a1, a2, a3):
        """
        """
        v1 = collections.Counter()
        v1[0] = 1
        v2 = v3 = 0
        for v4 in a1:
            v3 += -a3 if v4 == '0' else +a2
            v2 += v1[v3]
            v1[v3] += 1
        return v2

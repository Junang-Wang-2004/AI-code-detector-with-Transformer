class C1(object):

    def findThePrefixCommonArray(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        v2 = collections.Counter()
        v3 = 0
        for v4, (v5, v6) in enumerate(zip(a1, a2)):
            v2[v5] += 1
            if v2[v5] == 2:
                v3 += 1
            v2[v6] += 1
            if v2[v6] == 2:
                v3 += 1
            v1[v4] = v3
        return v1

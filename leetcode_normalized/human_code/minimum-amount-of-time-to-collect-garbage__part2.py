class C1(object):

    def garbageCollection(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in 'MPG':
            v3 = 0
            for v4 in range(len(a1)):
                v5 = a1[v4].count(v2)
                if v5:
                    v1 += v3 + v5
                    v3 = 0
                if v4 < len(a2):
                    v3 += a2[v4]
        return v1

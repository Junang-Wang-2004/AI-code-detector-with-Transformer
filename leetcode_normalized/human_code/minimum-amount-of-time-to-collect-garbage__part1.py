class C1(object):

    def garbageCollection(self, a1, a2):
        """
        """
        v1 = 0
        v2 = {}
        for v3 in range(len(a1)):
            for v4 in a1[v3]:
                v2[v4] = v3
            if v3 + 1 < len(a2):
                a2[v3 + 1] += a2[v3]
            v1 += len(a1[v3])
        v1 += sum((a2[v - 1] for v5, v6 in v2.items() if v6 - 1 >= 0))
        return v1

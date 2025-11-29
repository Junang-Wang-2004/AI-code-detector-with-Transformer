class C1(object):

    def maxTotal(self, a1, a2):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: (a2[x], -a1[x]))
        v2 = v3 = v4 = 0
        for v5 in v1:
            v6, v7 = (a2[v5], a1[v5])
            if v6 != v4:
                v3 = 0
                v4 = v6
            if v3 < v6:
                v2 += v7
                v3 += 1
        return v2

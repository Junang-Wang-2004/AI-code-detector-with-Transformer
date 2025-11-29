class C1(object):

    def resultsArray(self, a1, a2):
        """
        """
        v1 = [-1] * (len(a1) - a2 + 1)
        v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] - a1[v2] != v3 - v2:
                v2 = v3
            if v3 - v2 + 1 == a2:
                v1[v2] = a1[v3]
                v2 += 1
        return v1

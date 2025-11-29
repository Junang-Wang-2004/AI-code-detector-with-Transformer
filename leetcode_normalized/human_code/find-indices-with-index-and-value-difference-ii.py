class C1(object):

    def findIndices(self, a1, a2, a3):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1) - a2):
            if a1[v3] > a1[v1]:
                v1 = v3
            elif a1[v3] < a1[v2]:
                v2 = v3
            if a1[v1] - a1[v3 + a2] >= a3:
                return [v1, v3 + a2]
            if a1[v3 + a2] - a1[v2] >= a3:
                return [v2, v3 + a2]
        return [-1] * 2

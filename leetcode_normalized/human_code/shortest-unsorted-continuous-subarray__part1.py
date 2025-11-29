class C1(object):

    def findUnsortedSubarray(self, a1):
        """
        """
        v1 = len(a1)
        v2, v3 = (-1, -2)
        v4, v5 = (a1[-1], a1[0])
        for v6 in range(1, v1):
            v5 = max(v5, a1[v6])
            v4 = min(v4, a1[v1 - 1 - v6])
            if a1[v6] < v5:
                v3 = v6
            if a1[v1 - 1 - v6] > v4:
                v2 = v1 - 1 - v6

class C1(object):

    def minDistance(self, a1, a2, a3, a4, a5):
        """
        """

        def distance(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
        v1 = 0
        v2 = float('inf')
        for v3 in a5:
            v1 += distance(v3, a3) * 2
            v2 = min(v2, distance(v3, a4) - distance(v3, a3))
        return v1 + v2

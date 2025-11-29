class C1(object):

    def minimumDistance(self, a1):
        """
        """

        def distance(a1, a2):
            if -1 in [a1, a2]:
                return 0
            return abs(a1 // 6 - a2 // 6) + abs(a1 % 6 - a2 % 6)
        v1 = {(-1, -1): 0}
        for v2 in a1:
            v2 = ord(v2) - ord('A')
            v3 = {}
            for v4, v5 in v1:
                v3[v2, v5] = min(v3.get((v2, v5), float('inf')), v1[v4, v5] + distance(v4, v2))
                v3[v4, v2] = min(v3.get((v4, v2), float('inf')), v1[v4, v5] + distance(v5, v2))
            v1 = v3
        return min(v1.values())

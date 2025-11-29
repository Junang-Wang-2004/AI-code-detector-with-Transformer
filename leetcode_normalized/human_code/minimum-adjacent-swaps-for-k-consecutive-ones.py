class C1(object):

    def minMoves(self, a1, a2):
        """
        """

        def moves(a1, a2):
            return prefix[a2 + 1] - prefix[a1]
        v1 = [i for v2, v3 in enumerate(a1) if v3]
        v4 = [0] * (len(v1) + 1)
        for v2 in range(len(v1)):
            v4[v2 + 1] = v4[v2] + v1[v2]
        v5 = float('inf')
        for v2 in range(len(v1) - a2 + 1):
            v5 = min(v5, -moves(v2, v2 + a2 // 2 - 1) + moves(v2 + (a2 + 1) // 2, v2 + a2 - 1))
        v5 -= a2 // 2 * ((a2 + 1) // 2)
        return v5

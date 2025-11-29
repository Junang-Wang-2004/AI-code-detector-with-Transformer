class C1(object):

    def minimumMoves(self, a1):
        v1 = len(a1)
        v2 = {}

        def compute(a1, a2):
            if a1 > a2:
                return 0
            if a1 == a2:
                return 1
            v1 = (a1, a2)
            if v1 in v2:
                return v2[v1]
            v2 = 1 + compute(a1 + 1, a2)
            if a1 + 1 <= a2 and a1[a1] == a1[a1 + 1]:
                v2 = min(v2, 1 + compute(a1 + 2, a2))
            for v3 in range(a1 + 2, a2 + 1):
                if a1[a1] == a1[v3]:
                    v2 = min(v2, compute(a1 + 1, v3 - 1) + compute(v3 + 1, a2))
            v2[v1] = v2
            return v2
        return compute(0, v1 - 1)

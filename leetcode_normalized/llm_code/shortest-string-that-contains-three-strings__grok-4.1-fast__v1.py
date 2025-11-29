class C1:

    def minimumString(self, a1, a2, a3):

        def combine(a1, a2):
            if a1 in a2:
                return a2
            v1 = min(len(a1), len(a2))
            for v2 in range(v1, 0, -1):
                if a1[-v2:] == a2[:v2]:
                    return a1 + a2[v2:]
            return a1 + a2
        v1 = []
        for v2 in [[a1, a2, a3], [a1, a3, a2], [a2, a1, a3], [a2, a3, a1], [a3, a1, a2], [a3, a2, a1]]:
            v3 = combine(v2[0], v2[1])
            v4 = combine(v3, v2[2])
            v1.append(v4)
        return min(v1, key=lambda s: (len(s), s))

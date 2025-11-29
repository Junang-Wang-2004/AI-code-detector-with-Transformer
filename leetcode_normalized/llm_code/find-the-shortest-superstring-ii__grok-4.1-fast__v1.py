class C1:

    def shortestSuperstring(self, a1, a2):
        if a1 in a2:
            return a2
        if a2 in a1:
            return a1

        def max_prefix_overlap(a1, a2):
            v1, v2 = (len(a1), len(a2))
            for v3 in range(min(v1, v2), 0, -1):
                if a1[-v3:] == a2[:v3]:
                    return v3
            return 0
        v1 = max_prefix_overlap(a1, a2)
        v2 = max_prefix_overlap(a2, a1)
        v3 = a1 + a2[v1:]
        v4 = a2 + a1[v2:]
        return v3 if len(v3) <= len(v4) else v4

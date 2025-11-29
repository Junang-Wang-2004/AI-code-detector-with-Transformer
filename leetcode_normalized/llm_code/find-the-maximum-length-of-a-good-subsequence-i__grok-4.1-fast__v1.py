class C1:

    def maximumLength(self, a1, a2):
        v1 = {}
        v2 = 0
        v3 = len(a1)
        for v4 in a1:
            v1[v4] = v1.get(v4, 0) + 1
            if v1[v4] > v2:
                v2 = v1[v4]
        return min(v3, v2 + a2)

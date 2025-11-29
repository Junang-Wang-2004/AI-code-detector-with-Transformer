class C1:

    def minimumEffort(self, a1):
        v1 = sorted(a1, key=lambda t: t[1] - t[0])
        v2 = 0
        for v3, v4 in v1:
            v2 = max(v2 + v3, v4)
        return v2

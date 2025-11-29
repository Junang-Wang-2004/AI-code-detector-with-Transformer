class C1(object):

    def minimumRefill(self, a1, a2, a3):
        """
        """
        v1 = 0
        v2, v3 = (0, len(a1) - 1)
        v4, v5 = (a2, a3)
        while v2 < v3:
            if v4 < a1[v2]:
                v1 += 1
                v4 = a2
            v4 -= a1[v2]
            if v5 < a1[v3]:
                v1 += 1
                v5 = a3
            v5 -= a1[v3]
            v2, v3 = (v2 + 1, v3 - 1)
        if v2 == v3:
            if max(v4, v5) < a1[v2]:
                v1 += 1
        return v1

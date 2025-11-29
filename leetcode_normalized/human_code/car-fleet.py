class C1(object):

    def carFleet(self, a1, a2, a3):
        """
        """
        v1 = [float(a1 - p) / s for v2, v3 in sorted(zip(a2, a3))]
        v4, v5 = (0, 0)
        for v6 in reversed(v1):
            if v6 > v5:
                v4 += 1
                v5 = v6
        return v4

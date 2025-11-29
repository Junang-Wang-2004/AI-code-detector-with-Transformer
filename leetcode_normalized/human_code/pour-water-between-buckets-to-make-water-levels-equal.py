class C1(object):

    def equalizeWater(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            return sum((b - a3 for v1 in a1 if v1 - a3 > 0)) * a2 >= sum((a3 - v1 for v1 in a1 if a3 - v1 > 0))
        v1 = 1e-05
        v2 = (100 - a2) / 100.0
        v3, v4 = (float(min(a1)), float(sum(a1)) / len(a1))
        while v4 - v3 > v1:
            v5 = v3 + (v4 - v3) / 2
            if not check(a1, v2, v5):
                v4 = v5
            else:
                v3 = v5
        return v3

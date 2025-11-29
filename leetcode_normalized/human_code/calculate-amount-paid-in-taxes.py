class C1(object):

    def calculateTax(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3, v4 in a1:
            v1 += max((min(v3, a2) - v2) * v4 / 100.0, 0.0)
            v2 = v3
        return v1

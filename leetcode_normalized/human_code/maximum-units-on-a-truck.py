class C1(object):

    def maximumUnits(self, a1, a2):
        """
        """
        a1.sort(key=lambda x: x[1], reverse=True)
        v1 = 0
        for v2, v3 in a1:
            if a2 > v2:
                a2 -= v2
                v1 += v2 * v3
            else:
                v1 += a2 * v3
                break
        return v1

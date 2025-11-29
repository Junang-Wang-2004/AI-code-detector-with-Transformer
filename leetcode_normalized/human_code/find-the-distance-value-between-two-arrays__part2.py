class C1(object):

    def findTheDistanceValue(self, a1, a2, a3):
        """
        """
        (a1.sort(), a2.sort())
        v1, v2, v3 = (0, 0, 0)
        while v2 < len(a1) and v3 < len(a2):
            if a1[v2] - a2[v3] > a3:
                v3 += 1
                continue
            v1 += a2[v3] - a1[v2] > a3
            v2 += 1
        return v1 + len(a1) - v2

class C1(object):

    def arrayStringsAreEqual(self, a1, a2):
        """
        """
        v1 = v2 = v3 = v4 = 0
        while v3 < len(a1) and v4 < len(a2):
            if a1[v3][v1] != a2[v4][v2]:
                break
            v1 += 1
            if v1 == len(a1[v3]):
                v1 = 0
                v3 += 1
            v2 += 1
            if v2 == len(a2[v4]):
                v2 = 0
                v4 += 1
        return v3 == len(a1) and v4 == len(a2)

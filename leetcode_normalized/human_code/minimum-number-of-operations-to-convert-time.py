class C1(object):

    def convertTime(self, a1, a2):
        """
        """
        v1 = (60, 15, 5, 1)
        v2 = int(a2[:2]) * 60 + int(a2[3:]) - (int(a1[:2]) * 60 + int(a1[3:]))
        v3 = 0
        for v4 in v1:
            v5, v2 = divmod(v2, v4)
            v3 += v5
        return v3

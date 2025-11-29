class C1(object):

    def checkRecord(self, a1):
        """
        """
        v1 = 1000000007
        v2, v3, v4, v5, v6, v7 = (1, 0, 0, 0, 0, 0)
        for v8 in range(a1 + 1):
            v4, v3, v2 = (v3, v2, (v2 + v3 + v4) % v1)
            v7, v6, v5 = (v6, v5, (v2 + v5 + v6 + v7) % v1)
        return v5

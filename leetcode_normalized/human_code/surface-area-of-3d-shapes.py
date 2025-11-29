class C1(object):

    def surfaceArea(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            for v3 in range(len(a1)):
                if a1[v2][v3]:
                    v1 += 2 + a1[v2][v3] * 4
                if v2:
                    v1 -= min(a1[v2][v3], a1[v2 - 1][v3]) * 2
                if v3:
                    v1 -= min(a1[v2][v3], a1[v2][v3 - 1]) * 2
        return v1

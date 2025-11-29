class C1(object):

    def findRLEArray(self, a1, a2):
        """
        """
        v1 = []
        v2 = v3 = v4 = v5 = 0
        while (v4 or v2 < len(a1)) and (v5 or v3 < len(a2)):
            if not v4:
                v4 = a1[v2][1]
                v2 += 1
            if not v5:
                v5 = a2[v3][1]
                v3 += 1
            v6 = min(v4, v5)
            v4 -= v6
            v5 -= v6
            if v1 and v1[-1][0] == a1[v2 - 1][0] * a2[v3 - 1][0]:
                v1[-1][1] += v6
            else:
                v1.append([a1[v2 - 1][0] * a2[v3 - 1][0], v6])
        return v1

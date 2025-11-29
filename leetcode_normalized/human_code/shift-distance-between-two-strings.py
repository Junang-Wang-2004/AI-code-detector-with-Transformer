class C1(object):

    def shiftDistance(self, a1, a2, a3, a4):
        """
        """
        v1 = [0] * (len(a3) + 1)
        for v2 in range(len(a3)):
            v1[v2 + 1] = v1[v2] + a3[v2]
        v3 = [0] * (len(a4) + 1)
        for v2 in range(len(a4)):
            v3[v2 + 1] = v3[v2] + a4[v2]
        v4 = 0
        for v2 in range(len(a1)):
            if a1[v2] == a2[v2]:
                continue
            v5 = ord(a1[v2]) - ord('a')
            v6 = ord(a2[v2]) - ord('a')
            if v5 <= v6:
                v4 += min(v1[v6] - v1[v5], v3[-1] - (v3[v6 + 1] - v3[v5 + 1]))
            else:
                v4 += min(v3[v5 + 1] - v3[v6 + 1], v1[-1] - (v1[v5] - v1[v6]))
        return v4

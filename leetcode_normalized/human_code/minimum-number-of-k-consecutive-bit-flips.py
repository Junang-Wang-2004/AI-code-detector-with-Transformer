class C1(object):

    def minKBitFlips(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            if v3 >= a2:
                v2 -= a1[v3 - a2] // 2
            if v2 & 1 ^ a1[v3] == 0:
                if v3 + a2 > len(a1):
                    return -1
                a1[v3] += 2
                v2, v1 = (v2 + 1, v1 + 1)
        return v1

class C1(object):

    def longestOnes(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            a2 -= int(a1[v3] == 0)
            while a2 < 0:
                a2 += int(a1[v2] == 0)
                v2 += 1
            v1 = max(v1, v3 - v2 + 1)
        return v1

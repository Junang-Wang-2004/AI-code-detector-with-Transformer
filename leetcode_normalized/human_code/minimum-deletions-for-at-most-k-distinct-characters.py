class C1(object):

    def minDeletion(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = [0] * (max(v1) + 1)
        for v2 in v1:
            v3[v2] += 1
        v4 = 0
        v5 = 26 - a2
        for v6, v2 in enumerate(v3):
            v7 = min(v5, v2)
            v4 += v6 * v7
            v5 -= v7
            if v5 == 0:
                break
        return v4

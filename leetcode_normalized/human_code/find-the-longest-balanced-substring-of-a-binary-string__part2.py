class C1(object):

    def findTheLongestBalancedSubstring(self, a1):
        """
        """
        v1 = 0
        v2, v3 = ([0] * 2, [0] * 2)
        for v4 in a1:
            v3[int(v4)] += 1
            if v3[int(v4) ^ 1]:
                v2[int(v4) ^ 1], v3[int(v4) ^ 1] = (v3[int(v4) ^ 1], 0)
            v1 = max(v1, 2 * min(v2[0], v3[1]))
        return v1

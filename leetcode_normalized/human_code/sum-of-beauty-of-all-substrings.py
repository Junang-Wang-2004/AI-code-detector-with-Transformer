class C1(object):

    def beautySum(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = [0] * 26
            for v4 in range(v2, len(a1)):
                v3[ord(a1[v4]) - ord('a')] += 1
                v1 += max(v3) - min((x for v5 in v3 if v5))
        return v1

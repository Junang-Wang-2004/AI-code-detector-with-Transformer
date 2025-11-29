class C1(object):

    def longestAlternatingSubarray(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 > a2:
                v2 = 0
                continue
            if v2 % 2 == v3 % 2:
                v2 += 1
            else:
                v2 = int(v3 % 2 == 0)
            v1 = max(v1, v2)
        return v1

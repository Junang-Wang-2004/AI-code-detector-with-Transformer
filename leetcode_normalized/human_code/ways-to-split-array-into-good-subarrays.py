class C1(object):

    def numberOfGoodSubarraySplits(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (1, -1)
        for v4 in range(len(a1)):
            if a1[v4] != 1:
                continue
            if v3 != -1:
                v2 = v2 * (v4 - v3) % v1
            v3 = v4
        return v2 if v3 != -1 else 0

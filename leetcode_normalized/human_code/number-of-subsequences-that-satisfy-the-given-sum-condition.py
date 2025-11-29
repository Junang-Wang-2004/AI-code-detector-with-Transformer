class C1(object):

    def numSubseq(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = 0
        v3, v4 = (0, len(a1) - 1)
        while v3 <= v4:
            if a1[v3] + a1[v4] > a2:
                v4 -= 1
            else:
                v2 = (v2 + pow(2, v4 - v3, v1)) % v1
                v3 += 1
        return v2

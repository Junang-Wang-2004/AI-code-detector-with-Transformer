class C1(object):

    def nearestPalindromic(self, a1):
        """
        """
        v1 = len(a1)
        v2 = set((str(10 ** v1 + 1), str(10 ** (v1 - 1) - 1)))
        v3 = int(a1[:(v1 + 1) / 2])
        for v4 in map(str, (v3 - 1, v3, v3 + 1)):
            v2.add(v4 + [v4, v4[:-1]][v1 % 2][::-1])
        v2.discard(a1)
        return min(v2, key=lambda x: (abs(int(x) - int(a1)), int(x)))

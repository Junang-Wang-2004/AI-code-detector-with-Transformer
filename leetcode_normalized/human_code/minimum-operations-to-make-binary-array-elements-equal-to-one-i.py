class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1) - 2):
            if a1[v2]:
                continue
            a1[v2 + 1] ^= 1
            a1[v2 + 2] ^= 1
            v1 += 1
        return v1 if a1[-2] == a1[-1] == 1 else -1

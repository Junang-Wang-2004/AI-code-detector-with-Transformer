class C1(object):

    def subsequenceSumAfterCapping(self, a1, a2):
        """
        """
        v1 = [False] * len(a1)
        a1.sort()
        v2 = (1 << a2 + 1) - 1
        v3 = 1
        v4 = 0
        for v5 in range(1, len(a1) + 1):
            while v4 < len(a1) and a1[v4] < v5:
                v3 |= v3 << a1[v4] & v2
                v4 += 1
            for v6 in range(max(a2 % v5, a2 - (len(a1) - v4) * v5), a2 + 1, v5):
                if v3 & 1 << v6:
                    v1[v5 - 1] = True
                    break
        return v1

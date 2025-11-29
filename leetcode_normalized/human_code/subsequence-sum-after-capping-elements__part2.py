class C1(object):

    def subsequenceSumAfterCapping(self, a1, a2):
        """
        """
        v1 = [False] * len(a1)
        a1.sort()
        v2 = [False] * (a2 + 1)
        v2[0] = True
        v3 = 0
        for v4 in range(1, len(a1) + 1):
            while v3 < len(a1) and a1[v3] < v4:
                for v5 in reversed(range(a1[v3], a2 + 1)):
                    v2[v5] = v2[v5] or v2[v5 - a1[v3]]
                v3 += 1
            for v5 in range(max(a2 % v4, a2 - (len(a1) - v3) * v4), a2 + 1, v4):
                if v2[v5]:
                    v1[v4 - 1] = True
                    break
        return v1

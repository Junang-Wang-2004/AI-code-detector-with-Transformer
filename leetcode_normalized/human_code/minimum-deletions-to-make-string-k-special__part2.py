class C1(object):

    def minimumDeletions(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = sorted((v2 for v2 in v1 if v2))
        v4 = float('inf')
        v5 = v6 = 0
        v7 = len(a1)
        v8 = -1
        for v9 in range(len(v3)):
            if v9 + 1 < len(v3) and v3[v9 + 1] == v3[v9]:
                continue
            while v5 < len(v3) and v3[v5] <= v3[v9] + a2:
                v7 -= v3[v5]
                v5 += 1
            v4 = min(v4, v6 + (v7 - (v3[v9] + a2) * (len(v3) - v5)))
            v6 += v3[v9] * (v9 - v8)
            v8 = v9
        return v4

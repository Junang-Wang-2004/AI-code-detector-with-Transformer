class C1(object):

    def findLength(self, a1, a2):
        """
        """
        if len(a1) > len(a2):
            return self.findLength(a2, a1)

        def check(a1):
            v1 = set((a1[i:i + a1] for v2 in range(len(a1) - a1 + 1)))
            return any((a2[j:j + a1] in v1 for v3 in range(len(a2) - a1 + 1)))
        a1 = ''.join(map(chr, a1))
        a2 = ''.join(map(chr, a2))
        v3, v4 = (0, min(len(a1), len(a2)) + 1)
        while v3 < v4:
            v5 = v3 + (v4 - v3) / 2
            if not check(v5):
                v4 = v5
            else:
                v3 = v5 + 1
        return v3 - 1

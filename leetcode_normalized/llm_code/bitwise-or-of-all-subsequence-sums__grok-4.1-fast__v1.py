class C1:

    def subsequenceSumOr(self, a1):
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v2 += a1[v3]
            v1 |= v2 | a1[v3]
            v3 += 1
        return v1

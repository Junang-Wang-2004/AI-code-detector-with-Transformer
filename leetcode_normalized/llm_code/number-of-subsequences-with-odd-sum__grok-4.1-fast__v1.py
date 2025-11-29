class C1:

    def subsequenceCount(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        if v2 == 0:
            return 0
        v3 = any((num & 1 for v4 in a1))
        if not v3:
            return 0
        v5 = 1
        for v6 in range(v2 - 1):
            v5 = v5 * 2 % v1
        return v5

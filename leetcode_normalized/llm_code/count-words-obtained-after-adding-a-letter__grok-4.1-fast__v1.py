class C1:

    def wordCount(self, a1, a2):

        def get_mask(a1):
            v1 = 0
            for v2 in a1:
                v1 |= 1 << ord(v2) - ord('a')
            return v1
        v1 = {get_mask(p) for v2 in a1}
        v3 = 0
        for v4 in a2:
            v5 = get_mask(v4)
            if any((v5 ^ 1 << i in v1 for v6 in range(26) if v5 & 1 << v6)):
                v3 += 1
        return v3

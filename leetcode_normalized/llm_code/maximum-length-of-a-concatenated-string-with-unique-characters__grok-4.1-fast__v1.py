class C1(object):

    def maxLength(self, a1):

        def compute_mask(a1):
            v1 = 0
            for v2 in a1:
                v3 = ord(v2) - ord('a')
                v4 = 1 << v3
                if v1 & v4:
                    return 0
                v1 |= v4
            return v1
        v1 = [compute_mask(s) for v2 in a1]

        def backtrack(a1, a2, a3):
            if a1 == len(a1):
                return a3
            v1 = backtrack(a1 + 1, a2, a3)
            v2 = v1[a1]
            if v2 and a2 & v2 == 0:
                v1 = max(v1, backtrack(a1 + 1, a2 | v2, a3 + len(a1[a1])))
            return v1
        return backtrack(0, 0, 0)

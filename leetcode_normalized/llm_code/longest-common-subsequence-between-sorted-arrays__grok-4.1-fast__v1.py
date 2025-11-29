class C1(object):

    def longestCommomSubsequence(self, a1):
        if not a1:
            return []
        v1 = min(range(len(a1)), key=lambda k: len(a1[k]))
        v2 = a1[v1]
        if not v2:
            return []
        v3 = set(v2)
        for v4 in a1:
            v3 &= set(v4)
            if not v3:
                return []
        return [elem for v5 in v2 if v5 in v3]

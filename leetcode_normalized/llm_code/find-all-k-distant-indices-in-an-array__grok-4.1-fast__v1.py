class C1(object):

    def findKDistantIndices(self, a1, a2, a3):
        v1 = [idx for v2, v3 in enumerate(a1) if v3 == a2]
        if not v1:
            return []
        v4 = []
        v5 = max(0, v1[0] - a3)
        v6 = min(len(a1) - 1, v1[0] + a3)
        for v2 in v1[1:]:
            v7 = max(0, v2 - a3)
            v8 = min(len(a1) - 1, v2 + a3)
            if v7 > v6 + 1:
                v4.extend(range(v5, v6 + 1))
                v5 = v7
                v6 = v8
            else:
                v6 = max(v6, v8)
        v4.extend(range(v5, v6 + 1))
        return v4

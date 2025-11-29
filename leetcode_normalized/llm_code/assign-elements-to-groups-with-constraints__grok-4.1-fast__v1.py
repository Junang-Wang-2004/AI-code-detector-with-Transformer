class C1(object):

    def assignElements(self, a1, a2):
        if not a1:
            return []
        v1 = max(a1)
        v2 = [-1] * (v1 + 1)
        for v3, v4 in enumerate(a2):
            if v4 > v1 or v2[v4] != -1:
                continue
            v5 = v4
            while v5 <= v1:
                if v2[v5] == -1:
                    v2[v5] = v3
                v5 += v4
        return [v2[g] for v6 in a1]

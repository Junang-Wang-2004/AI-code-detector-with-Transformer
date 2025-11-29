class C1:

    def isReflected(self, a1):
        if not a1:
            return True
        v1 = set((tuple(pt) for v2 in a1))
        v3 = min((v2[0] for v2 in a1))
        v4 = max((v2[0] for v2 in a1))
        v5 = v3 + v4
        for v2 in a1:
            v6, v7 = v2
            v8 = v5 - v6
            if (v8, v7) not in v1:
                return False
        return True

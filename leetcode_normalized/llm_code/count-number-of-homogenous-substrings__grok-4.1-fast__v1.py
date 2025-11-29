class C1:

    def countHomogenous(self, a1):
        v1 = 1000000007
        v2 = 0
        v3 = None
        v4 = 0
        for v5 in a1:
            if v5 == v3:
                v4 += 1
            else:
                if v3 is not None:
                    v2 = (v2 + v4 * (v4 + 1) // 2) % v1
                v3 = v5
                v4 = 1
        if v3 is not None:
            v2 = (v2 + v4 * (v4 + 1) // 2) % v1
        return v2

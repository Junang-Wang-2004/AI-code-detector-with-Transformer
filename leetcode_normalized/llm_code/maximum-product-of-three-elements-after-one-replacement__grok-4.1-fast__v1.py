class C1:

    def maxProduct(self, a1):
        v1 = 0
        v2 = 0
        for v3 in a1:
            v4 = abs(v3)
            if v4 > v1:
                v2 = v1
                v1 = v4
            elif v4 > v2:
                v2 = v4
        return v1 * v2 * 100000

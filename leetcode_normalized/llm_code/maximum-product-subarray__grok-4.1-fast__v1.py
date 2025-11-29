class C1:

    def maxProduct(self, a1):
        v1 = a1[0]
        v2 = a1[0]
        v3 = a1[0]
        for v4 in a1[1:]:
            v5 = v2 * v4
            v6 = v3 * v4
            v7 = v4
            v8 = v4
            if v5 > v7:
                v7 = v5
            if v6 > v7:
                v7 = v6
            if v5 < v8:
                v8 = v5
            if v6 < v8:
                v8 = v6
            v2 = v7
            v3 = v8
            if v7 > v1:
                v1 = v7
        return v1

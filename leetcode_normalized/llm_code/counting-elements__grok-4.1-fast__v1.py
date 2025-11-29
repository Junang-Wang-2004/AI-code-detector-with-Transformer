class C1:

    def countElements(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = 0
        for v2 in v1:
            if v2 + 1 in v1:
                v3 += v1[v2]
        return v3

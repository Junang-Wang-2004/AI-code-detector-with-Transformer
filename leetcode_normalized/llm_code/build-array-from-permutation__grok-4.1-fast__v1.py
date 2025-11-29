class C1:

    def buildArray(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        for v3 in range(v1):
            v2[v3] = a1[a1[v3]]
        return v2

class C1:

    def createTargetArray(self, a1, a2):
        v1 = []
        v2 = len(a1)
        for v3 in range(v2):
            v4 = a2[v3]
            v1 = v1[:v4] + [a1[v3]] + v1[v4:]
        return v1

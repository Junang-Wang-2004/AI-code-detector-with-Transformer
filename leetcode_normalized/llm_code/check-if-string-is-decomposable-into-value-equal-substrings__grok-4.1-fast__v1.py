class C1:

    def isDecomposable(self, a1):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while v1 < v3:
            v4 = v1
            while v1 < v3 and a1[v1] == a1[v4]:
                v1 += 1
            v5 = v1 - v4
            if v5 not in (2, 3):
                return False
            if v5 == 2:
                v2 += 1
        return v2 == 1

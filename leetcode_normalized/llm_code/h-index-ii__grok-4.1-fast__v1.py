class C1:

    def hIndex(self, a1):
        v1 = len(a1)
        v2, v3 = (0, v1)
        while v2 < v3:
            v4 = v2 + (v3 - v2 + 1) // 2
            if a1[v1 - v4] >= v4:
                v2 = v4
            else:
                v3 = v4 - 1
        return v2

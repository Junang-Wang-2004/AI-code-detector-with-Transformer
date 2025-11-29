class C1:

    def missingElement(self, a1, a2):
        v1, v2 = (0, len(a1))
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if a1[v3] - v3 - 1 < a2:
                v1 = v3 + 1
            else:
                v2 = v3
        return a2 + v1

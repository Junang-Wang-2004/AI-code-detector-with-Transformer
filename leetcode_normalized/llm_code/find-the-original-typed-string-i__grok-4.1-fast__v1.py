class C1:

    def possibleStringCount(self, a1):
        v1 = 0
        for v2, v3 in zip(a1, a1[1:]):
            if v2 == v3:
                v1 += 1
        return v1 + 1

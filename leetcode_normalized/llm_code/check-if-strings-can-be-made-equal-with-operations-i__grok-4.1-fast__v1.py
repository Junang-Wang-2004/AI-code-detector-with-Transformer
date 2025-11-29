class C1:

    def canBeEqual(self, a1, a2):
        v1 = sorted(a1[0] + a1[2])
        v2 = sorted(a2[0] + a2[2])
        v3 = sorted(a1[1] + a1[3])
        v4 = sorted(a2[1] + a2[3])
        return v1 == v2 and v3 == v4

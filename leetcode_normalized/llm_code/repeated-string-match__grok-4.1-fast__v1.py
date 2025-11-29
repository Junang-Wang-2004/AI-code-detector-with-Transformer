class C1:

    def repeatedStringMatch(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = (v2 + v1 - 1) // v1
        v4 = a1 * v3
        if a2 in v4:
            return v3
        v4 += a1
        if a2 in v4:
            return v3 + 1
        return -1

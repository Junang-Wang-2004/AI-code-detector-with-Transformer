class C1:

    def differenceOfSums(self, a1, a2):
        v1 = a1 * (a1 + 1) // 2
        v2 = a1 // a2
        v3 = a2 * v2 * (v2 + 1) // 2
        return v1 - 2 * v3

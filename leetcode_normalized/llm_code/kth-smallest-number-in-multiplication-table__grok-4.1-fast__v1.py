class C1:

    def findKthNumber(self, a1, a2, a3):

        def numbers_leq(a1):
            v1 = 0
            for v2 in range(1, a1 + 1):
                v1 += min(a2, a1 // v2)
            return v1
        v1 = 1
        v2 = a1 * a2
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if numbers_leq(v3) >= a3:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1

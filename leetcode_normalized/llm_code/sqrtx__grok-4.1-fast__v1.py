class C1:

    def mySqrt(self, a1):
        v1, v2 = (0, a1)
        while v1 <= v2:
            v3 = (v1 + v2) // 2
            if v3 * v3 <= a1:
                v1 = v3 + 1
            else:
                v2 = v3 - 1
        return v2

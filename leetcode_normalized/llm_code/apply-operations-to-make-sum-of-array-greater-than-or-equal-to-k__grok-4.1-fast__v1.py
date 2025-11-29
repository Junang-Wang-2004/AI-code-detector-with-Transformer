class C1:

    def minOperations(self, a1):
        v1, v2 = (0, a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if v3 * v3 <= a1:
                v1 = v3 + 1
            else:
                v2 = v3 - 1
        v4 = v2
        v5 = (a1 + v4 - 1) // v4
        return v4 + v5 - 2

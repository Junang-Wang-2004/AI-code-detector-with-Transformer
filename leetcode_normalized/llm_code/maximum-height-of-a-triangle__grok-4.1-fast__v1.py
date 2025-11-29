class C1:

    def maxHeightOfTriangle(self, a1: int, a2: int) -> int:

        def feasible(a1: int) -> bool:
            v1 = (a1 + 1) // 2
            v2 = a1 // 2
            v3 = v1 * v1
            v4 = v2 * (v2 + 1)
            return a1 >= v3 and a2 >= v4 or (a1 >= v4 and a2 >= v3)
        v1, v2 = (0, 2000000000)
        while v1 < v2:
            v3 = (v1 + v2 + 1) // 2
            if feasible(v3):
                v1 = v3
            else:
                v2 = v3 - 1
        return v1

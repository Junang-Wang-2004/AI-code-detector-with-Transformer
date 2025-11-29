class C1:

    def maxValue(self, a1: int, a2: int, a3: int) -> int:
        v1 = a3 - a1
        v2 = 0
        v3 = v1
        while v2 < v3:
            v4 = (v2 + v3 + 1) // 2
            if self._feasible(v4, a2, a1 - a2, v1):
                v2 = v4
            else:
                v3 = v4 - 1
        return v2 + 1

    def _feasible(self, a1: int, a2: int, a3: int, a4: int) -> bool:

        def side(a1: int, a2: int) -> int:
            if a1 < 0:
                return 0
            v1 = max(0, a1 - (a2 - 1))
            v2 = a1 - v1 + 1
            return (a1 + v1) * v2 // 2
        v1 = side(a1, a2)
        v2 = side(a1, a3)
        return v1 + v2 - a1 <= a4

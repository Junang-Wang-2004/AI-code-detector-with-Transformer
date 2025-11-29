class C1:

    def clumsy(self, a1: int) -> int:
        if a1 <= 4:
            return [0, 1, 2, 6, 7][a1]
        v1 = a1 % 4
        if v1 == 3:
            return a1 - 1
        return a1 + 1 + (1 if v1 else 0)

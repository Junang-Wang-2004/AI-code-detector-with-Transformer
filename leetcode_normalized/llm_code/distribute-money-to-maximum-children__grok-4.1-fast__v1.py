class C1:

    def distMoney(self, a1: int, a2: int) -> int:
        if a1 < a2:
            return -1
        v1 = a1 - a2
        v2 = v1 // 7
        v3 = v1 % 7
        if v2 > a2:
            v2 = a2 - 1
        elif v2 == a2:
            if v3 != 0:
                v2 -= 1
        elif v2 == a2 - 1:
            if v3 == 3:
                v2 -= 1
        return v2

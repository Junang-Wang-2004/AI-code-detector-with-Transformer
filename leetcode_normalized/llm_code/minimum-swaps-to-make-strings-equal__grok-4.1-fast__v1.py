class C1:

    def minimumSwap(self, a1: str, a2: str) -> int:
        v1 = 0
        v2 = 0
        for v3, v4 in zip(a1, a2):
            if v3 == 'x' and v4 == 'y':
                v1 += 1
            elif v3 == 'y' and v4 == 'x':
                v2 += 1
        if v1 % 2 != v2 % 2:
            return -1
        v5 = v1 + v2
        return v5 // 2 + v1 % 2

class C1:

    def minimumSteps(self, a1: str) -> int:
        v1 = 0
        v2 = 0
        for v3 in a1:
            if v3 == '0':
                v1 += v2
            else:
                v2 += 1
        return v1

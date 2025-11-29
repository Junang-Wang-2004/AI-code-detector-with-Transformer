class C1:

    def areNumbersAscending(self, a1: str) -> bool:
        v1 = -1
        v2 = 0
        v3 = False
        for v4 in a1:
            if v4.isdigit():
                if not v3:
                    v3 = True
                    v2 = 0
                v2 = v2 * 10 + int(v4)
            elif v3:
                if v2 <= v1:
                    return False
                v1 = v2
                v3 = False
        return not v3 or v2 > v1

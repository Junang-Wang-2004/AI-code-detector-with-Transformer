class C1:

    def makeTheIntegerZero(self, a1, a2):
        v1 = 0
        while v1 < 61:
            v1 += 1
            v2 = a1 - v1 * a2
            if v2 < 0:
                break
            v3 = bin(v2).count('1')
            if v3 <= v1 <= v2:
                return v1
        return -1

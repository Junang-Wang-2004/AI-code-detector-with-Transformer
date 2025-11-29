class C1:

    def canAliceWin(self, a1):
        v1 = sum(a1)
        v2 = sum((n for v3 in a1 if v3 < 10))
        return 2 * v2 != v1

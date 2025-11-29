class C1:

    def canMakeArithmeticProgression(self, a1):
        a1.sort()
        v1 = a1[1] - a1[0]
        for v2 in range(2, len(a1)):
            if a1[v2] - a1[v2 - 1] != v1:
                return False
        return True

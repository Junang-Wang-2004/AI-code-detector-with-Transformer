class C1:

    def findTheWinner(self, a1, a2):
        v1 = 0
        for v2 in range(2, a1 + 1):
            v1 = (v1 + a2) % v2
        return v1 + 1

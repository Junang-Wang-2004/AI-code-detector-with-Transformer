class C1:

    def findGameWinner(self, a1):
        v1 = a1 % 6
        return v1 == 0 or v1 > 1

class C1(object):

    def __init__(self):
        self.__lookup = {(0, 0): 0, (1, 1): 2, (1, 0): 3}

    def minKnightMoves(self, a1, a2):
        """
        """

        def dp(a1, a2):
            a1, a2 = (abs(a1), abs(a2))
            if a1 < a2:
                a1, a2 = (a2, a1)
            if (a1, a2) not in self.__lookup:
                self.__lookup[a1, a2] = min(dp(a1 - 1, a2 - 2), dp(a1 - 2, a2 - 1)) + 1
            return self.__lookup[a1, a2]
        return dp(a1, a2)

class C1(object):

    def numOfBurgers(self, a1, a2):
        """
        """
        return [a1 // 2 - a2, 2 * a2 - a1 // 2] if a1 % 2 == 0 and 2 * a2 <= a1 <= 4 * a2 else []

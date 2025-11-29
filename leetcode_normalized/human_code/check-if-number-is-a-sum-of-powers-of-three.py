class C1(object):

    def checkPowersOfThree(self, a1):
        """
        """
        while a1 > 0:
            if a1 % 3 == 2:
                return False
            a1 //= 3
        return True

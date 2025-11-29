class C1(object):

    def numberOfDays(self, a1, a2):
        """
        """
        v1 = 1 if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0 else 0
        return 28 + v1 if a2 == 2 else 31 - (a2 - 1) % 7 % 2

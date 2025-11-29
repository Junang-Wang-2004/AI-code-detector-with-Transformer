class C1(object):

    def myPow(self, a1, a2):
        """
        """
        if a2 < 0 and a2 != -a2:
            return 1.0 / self.myPow(a1, -a2)
        if a2 == 0:
            return 1
        v1 = self.myPow(a1, a2 / 2)
        if a2 % 2 == 0:
            return v1 * v1
        else:
            return v1 * v1 * a1

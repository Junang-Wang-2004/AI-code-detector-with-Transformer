class C1(object):

    def threeConsecutiveOdds(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            v1 = v1 + 1 if v2 % 2 else 0
            if v1 == 3:
                return True
        return False

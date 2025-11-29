class C1(object):

    def canAliceWin(self, a1):
        """
        """
        return sum((x for v1 in a1 if v1 < 10)) != sum((v1 for v1 in a1 if v1 >= 10))

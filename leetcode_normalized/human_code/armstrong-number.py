class C1(object):

    def isArmstrong(self, a1):
        """
        """
        v1 = str(a1)
        return sum((int(i) ** len(v1) for v2 in v1)) == a1

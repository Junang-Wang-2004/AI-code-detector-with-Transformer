class C1(object):

    def hasAlternatingBits(self, a1):
        """
        """
        a1, v2 = divmod(a1, 2)
        while a1 > 0:
            if v2 == a1 % 2:
                return False
            a1, v2 = divmod(a1, 2)
        return True

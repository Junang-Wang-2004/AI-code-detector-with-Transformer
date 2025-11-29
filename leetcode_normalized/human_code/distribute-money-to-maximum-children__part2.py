class C1(object):

    def distMoney(self, a1, a2):
        """
        """
        if a1 < a2 * 1:
            return -1
        a1 -= a2 * 1
        v2, v3 = divmod(a1, 7)
        if v2 > a2:
            return a2 - 1
        if v2 == a2:
            return v2 - int(v3 != 0)
        if v2 == a2 - 1:
            return v2 - int(v3 == 3)
        return v2

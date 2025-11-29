class C1(object):

    def distMoney(self, a1, a2):
        """
        """
        if a1 < a2 * 1:
            return -1
        a1 -= a2 * 1
        v2, v3 = divmod(a1, 7)
        return min(v2, a2) - int(v2 > a2 or (v2 == a2 and v3 != 0) or (v2 == a2 - 1 and v3 == 3))

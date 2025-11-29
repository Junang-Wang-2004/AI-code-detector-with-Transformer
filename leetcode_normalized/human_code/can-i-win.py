class C1(object):

    def canIWin(self, a1, a2):
        """
        """

        def canIWinHelper(a1, a2, a3, a4):
            if a3 in a4:
                return a4[a3]
            v1 = 1
            for v2 in range(a1):
                if a3 & v1 == 0:
                    if v2 + 1 >= a2 or not canIWinHelper(a1, a2 - (v2 + 1), a3 | v1, a4):
                        a4[a3] = True
                        return True
                v1 <<= 1
            a4[a3] = False
            return False
        if (1 + a1) * (a1 / 2) < a2:
            return False
        return canIWinHelper(a1, a2, 0, {})

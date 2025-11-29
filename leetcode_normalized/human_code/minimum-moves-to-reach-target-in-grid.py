class C1(object):

    def minMoves(self, a1, a2, a3, a4):
        """
        """
        v1 = 0
        while (a1, a2) != (a3, a4):
            if not (a1 <= a3 and a2 <= a4):
                return -1
            if a3 < a4:
                if a3 > a4 - a3:
                    a4 -= a3
                else:
                    if a4 % 2:
                        return -1
                    a4 -= a4 // 2
            elif a3 > a4:
                if a4 > a3 - a4:
                    a3 -= a4
                else:
                    if a3 % 2:
                        return -1
                    a3 -= a3 // 2
            elif a1 == 0:
                a3 -= a4
            elif a2 == 0:
                a4 -= a3
            else:
                return -1
            v1 += 1
        return v1

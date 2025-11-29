class C1(object):

    def checkMove(self, a1, a2, a3, a4):
        """
        """

        def check(a1, a2, a3, a4, a5, a6):
            v1 = 2
            while 0 <= a3 < len(a1) and 0 <= a4 < len(a1[0]) and (a1[a3][a4] != '.'):
                if a1[a3][a4] == a2:
                    return v1 >= 3
                a3 += a5
                a4 += a6
                v1 += 1
            return False
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        for v2, v3 in v1:
            v4, v5 = (a2 + v2, a3 + v3)
            if check(a1, a4, v4, v5, v2, v3):
                return True
        return False

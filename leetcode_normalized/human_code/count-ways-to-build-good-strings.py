class C1(object):

    def countGoodStrings(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = [0] * (a2 + 1)
        v3[0] = 1
        for v4 in range(1, a2 + 1):
            if v4 >= a3:
                v3[v4] = (v3[v4] + v3[v4 - a3]) % v1
            if v4 >= a4:
                v3[v4] = (v3[v4] + v3[v4 - a4]) % v1
            if v4 >= a1:
                v2 = (v2 + v3[v4]) % v1
        return v2

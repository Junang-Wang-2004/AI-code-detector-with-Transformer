class C1(object):

    def numberOfWays(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = v3 = v4 = v5 = 0
        if a4 == a5:
            v2 = 1
        elif a4[0] == a5[0]:
            v3 = 1
        elif a4[1] == a5[1]:
            v4 = 1
        else:
            v5 = 1
        for v6 in range(a3):
            v2, v3, v4, v5 = ((v3 + v4) % v1, (v2 * (a2 - 1) + v3 * (a2 - 2) + v5) % v1, (v2 * (a1 - 1) + v4 * (a1 - 2) + v5) % v1, (v3 * (a1 - 1) + v4 * (a2 - 1) + v5 * (a1 - 2 + (a2 - 2))) % v1)
        return v2

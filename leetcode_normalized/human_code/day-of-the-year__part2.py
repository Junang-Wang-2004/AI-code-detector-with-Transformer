class C1(object):

    def dayOfYear(self, a1):
        """
        """

        def numberOfDays(a1, a2):
            v1 = 1 if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0 else 0
            return 28 + v1 if a2 == 2 else 31 - (a2 - 1) % 7 % 2
        v1, v2, v3 = list(map(int, a1.split('-')))
        for v4 in range(1, v2):
            v3 += numberOfDays(v1, v4)
        return v3

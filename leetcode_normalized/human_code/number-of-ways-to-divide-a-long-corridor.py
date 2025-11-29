class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = (1, 0, -1)
        for v5, v6 in enumerate(a1):
            if v6 != 'S':
                continue
            v3 += 1
            if v3 >= 3 and v3 % 2:
                v2 = v2 * (v5 - v4) % v1
            v4 = v5
        return v2 if v3 and v3 % 2 == 0 else 0

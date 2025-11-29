class C1(object):

    def numWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = a1.count('1')
        if v2 % 3:
            return 0
        v2 //= 3
        if v2 == 0:
            return (len(a1) - 1) * (len(a1) - 2) // 2 % v1
        v3 = v4 = v5 = 0
        for v6 in a1:
            if v6 == '1':
                v3 += 1
            if v3 == v2:
                v4 += 1
            elif v3 == 2 * v2:
                v5 += 1
        return v4 * v5 % v1

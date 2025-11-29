class C1(object):

    def concatenatedBinary(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = v3 = 0
        for v4 in range(1, a1 + 1):
            if v4 & v4 - 1 == 0:
                v3 += 1
            v2 = ((v2 << v3) % v1 + v4) % v1
        return v2

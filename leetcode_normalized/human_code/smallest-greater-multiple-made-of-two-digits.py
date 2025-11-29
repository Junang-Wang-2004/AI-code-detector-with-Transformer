class C1(object):

    def findInteger(self, a1, a2, a3):
        """
        """
        v1 = 10
        v2 = 2 ** 31 - 1
        if a2 < a3:
            a2, a3 = (a3, a2)
        v5 = 2
        for v6 in range(1, v1 + 1):
            for v7 in range(v5):
                v8, v9 = (0, v5 >> 1)
                while v9:
                    v8 = v8 * 10 + (a2 if v7 & v9 else a3)
                    v9 >>= 1
                if a1 < v8 <= v2 and v8 % a1 == 0:
                    return v8
            v5 <<= 1
        return -1

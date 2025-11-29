class C1(object):

    def minimizeXor(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1)[2:].count('1')
        v1, v2 = (popcount(a1), popcount(a2))
        v3 = a1
        v4 = abs(v1 - v2)
        v5 = 1 if v1 >= v2 else 0
        v6 = 0
        while v4:
            if a1 >> v6 & 1 == v5:
                v4 -= 1
                v3 ^= 1 << v6
            v6 += 1
        return v3

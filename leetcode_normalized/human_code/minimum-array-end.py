class C1(object):

    def minEnd(self, a1, a2):
        """
        """
        a1 -= 1
        v2 = v3 = 1
        while v2 <= a1:
            if a2 & v3 == 0:
                if a1 & v2:
                    a2 |= v3
                v2 <<= 1
            v3 <<= 1
        return a2

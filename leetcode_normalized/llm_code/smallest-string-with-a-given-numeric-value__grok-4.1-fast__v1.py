class C1(object):

    def getSmallestString(self, a1, a2):
        """
        """
        v1 = []
        for v2 in range(a1):
            v3 = a1 - v2 - 1
            v4 = max(1, a2 - 26 * v3)
            v1.append(chr(ord('a') + v4 - 1))
            a2 -= v4
        return ''.join(v1)

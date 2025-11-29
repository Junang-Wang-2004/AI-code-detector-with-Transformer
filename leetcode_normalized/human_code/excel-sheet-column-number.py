class C1(object):

    def titleToNumber(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v1 *= 26
            v1 += ord(a1[v2]) - ord('A') + 1
        return v1

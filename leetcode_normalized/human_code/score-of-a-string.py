class C1(object):

    def scoreOfString(self, a1):
        """
        """
        return sum((abs(ord(a1[i + 1]) - ord(a1[i])) for v1 in range(len(a1) - 1)))

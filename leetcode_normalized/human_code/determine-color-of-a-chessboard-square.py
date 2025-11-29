class C1(object):

    def squareIsWhite(self, a1):
        """
        """
        return (ord(a1[0]) - ord('a')) % 2 != (ord(a1[1]) - ord('1')) % 2

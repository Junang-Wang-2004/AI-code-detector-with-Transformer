class C1(object):

    def cellsInRange(self, a1):
        """
        """
        return [chr(x) + chr(y) for v1 in range(ord(a1[0]), ord(a1[3]) + 1) for v2 in range(ord(a1[1]), ord(a1[4]) + 1)]

class C1(object):

    def sortEvenOdd(self, a1):
        """
        """
        a1[::2], a1[1::2] = (sorted(a1[::2]), sorted(a1[1::2], reverse=True))
        return a1

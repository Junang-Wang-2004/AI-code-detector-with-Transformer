class C1(object):

    def countOperations(self, a1, a2):
        """
        """
        v1 = 0
        while a2:
            v1 += a1 // a2
            a1, a2 = (a2, a1 % a2)
        return v1

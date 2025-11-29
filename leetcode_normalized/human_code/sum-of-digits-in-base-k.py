class C1(object):

    def sumBase(self, a1, a2):
        """
        """
        v1 = 0
        while a1:
            a1, v3 = divmod(a1, a2)
            v1 += v3
        return v1

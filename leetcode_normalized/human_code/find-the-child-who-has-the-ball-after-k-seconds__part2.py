class C1(object):

    def numberOfChild(self, a1, a2):
        """
        """
        v1 = a2 % (2 * (a1 - 1))
        return v1 if v1 <= a1 - 1 else a1 - 1 - (v1 - (a1 - 1))

class C1(object):

    def numberOfChild(self, a1, a2):
        """
        """
        v1, v2 = divmod(a2, a1 - 1)
        return v2 if v1 & 1 == 0 else a1 - 1 - v2

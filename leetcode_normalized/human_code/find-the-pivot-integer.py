class C1(object):

    def pivotInteger(self, a1):
        """
        """
        v1 = int(((a1 + 1) * a1 // 2) ** 0.5 + 0.5)
        return v1 if v1 ** 2 == (a1 + 1) * a1 // 2 else -1

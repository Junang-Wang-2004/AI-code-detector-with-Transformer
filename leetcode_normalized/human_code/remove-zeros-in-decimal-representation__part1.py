class C1(object):

    def removeZeros(self, a1):
        """
        """

        def reverse(a1):
            v1 = 0
            while a1:
                a1, v3 = divmod(a1, 10)
                v1 = v1 * 10 + v3
            return v1
        v1 = 0
        while a1:
            a1, v3 = divmod(a1, 10)
            if v3:
                v1 = v1 * 10 + v3
        return reverse(v1)

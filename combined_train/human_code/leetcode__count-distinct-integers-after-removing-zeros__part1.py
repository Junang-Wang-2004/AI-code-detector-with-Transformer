class C1(object):

    def countDistinct(self, a1):
        """
        """

        def reverse(a1):
            v1, v2 = (0, 1)
            while a1:
                a1, v4 = divmod(a1, 10)
                v1 = v1 * 10 + v4
                v2 *= 9
            return (v1, v2)
        v1, v2 = reverse(a1 + 1)
        v3 = (v2 - 9) // (9 - 1)
        v2 //= 9
        while v2:
            v1, v4 = divmod(v1, 10)
            if v4 == 0:
                break
            v3 += (v4 - 1) * v2
            v2 //= 9
        return v3

class C1(object):

    def isFascinating(self, a1):
        """
        """
        v1 = [0]

        def check(a1):
            while a1:
                a1, v2 = divmod(a1, 10)
                if v2 == 0 or v1[0] & 1 << v2:
                    return False
                v1[0] |= 1 << v2
            return True
        return check(a1) and check(2 * a1) and check(3 * a1)

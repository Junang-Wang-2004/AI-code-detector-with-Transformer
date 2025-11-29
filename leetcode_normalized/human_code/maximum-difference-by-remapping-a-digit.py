class C1(object):

    def minMaxDifference(self, a1):
        """
        """

        def f(a1):
            v1 = 0
            v2 = 1
            while v2 <= a1:
                v2 *= 10
            v2 //= 10
            v3 = -1
            while v2:
                v4 = a1 // v2 % 10
                if v3 == -1 and v4 != a1:
                    v3 = v4
                v1 += v2 * (a1 if v4 == v3 else v4)
                v2 //= 10
            return v1
        return f(9) - f(0)

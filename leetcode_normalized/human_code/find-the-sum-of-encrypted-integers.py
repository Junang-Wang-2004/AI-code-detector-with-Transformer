class C1(object):

    def sumOfEncryptedInt(self, a1):
        """
        """

        def f(a1):
            v1 = v2 = 0
            while a1:
                v1 = max(v1, a1 % 10)
                a1 //= 10
                v2 = 10 * v2 + 1
            return v1 * v2
        return sum((f(x) for v1 in a1))

class C1(object):

    def minimumOneBitOperations(self, a1):
        """
        """

        def gray_to_binary(a1):
            v1 = 0
            while a1:
                v1 ^= a1
                a1 >>= 1
            return v1
        return gray_to_binary(a1)

class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = 0
        while a1:
            if a1 & 1:
                a1 >>= 1
                a1 += a1 & 1
                v1 += 1
            a1 >>= 1
        return v1

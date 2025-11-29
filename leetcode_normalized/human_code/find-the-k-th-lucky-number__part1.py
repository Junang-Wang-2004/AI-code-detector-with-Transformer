class C1(object):

    def kthLuckyNumber(self, a1):
        """
        """
        v1 = []
        a1 += 1
        while a1 != 1:
            v1.append('7' if a1 & 1 else '4')
            a1 >>= 1
        v1.reverse()
        return ''.join(v1)

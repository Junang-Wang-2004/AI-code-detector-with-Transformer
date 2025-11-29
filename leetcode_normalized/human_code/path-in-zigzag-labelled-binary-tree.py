class C1(object):

    def pathInZigZagTree(self, a1):
        """
        """
        v1 = 2 ** a1.bit_length()
        v2 = []
        while a1 >= 1:
            v2.append(a1)
            a1 = (v1 // 2 + (v1 - 1 - a1)) // 2
            v1 //= 2
        v2.reverse()
        return v2

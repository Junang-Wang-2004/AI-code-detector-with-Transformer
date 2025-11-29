class C1(object):

    def findKthBit(self, a1, a2):
        """
        """
        v1, v2 = (0, 2 ** a1 - 1)
        while a2 > 1:
            if a2 == v2 // 2 + 1:
                v1 ^= 1
                break
            if a2 > v2 // 2:
                a2 = v2 + 1 - a2
                v1 ^= 1
            v2 //= 2
        return str(v1)

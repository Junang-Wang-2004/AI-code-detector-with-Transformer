class C1(object):

    def findKthBit(self, a1, a2):
        v1 = 0
        v2 = a2
        v3 = a1
        while v3 > 1:
            v4 = 1 << v3 - 1
            if v2 == v4:
                v1 ^= 1
                break
            if v2 > v4:
                v2 = (1 << v3) - v2
                v1 ^= 1
            v3 -= 1
        return '1' if v1 & 1 else '0'

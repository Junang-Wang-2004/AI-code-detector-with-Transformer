from functools import reduce

class C1(object):

    def findNumber(self):
        """
        """
        v1 = 30
        v2 = 0
        v3 = commonBits(0)
        for v4 in range(v1):
            v5 = commonBits(1 << v4)
            if v5 - v3 == 1:
                v2 |= 1 << v4
            v3 = v5
        return v2

import collections

class C1(object):

    def singleNumber(self, a1):
        v1, v2, v3 = (0, 0, 0)
        for v4 in a1:
            v1, v2, v3 = (~v4 & v1 | v4 & ~v1 & ~v2 & ~v3, ~v4 & v2 | v4 & v1, ~v4 & v3 | v4 & v2)
        return v2

import collections

class C1(object):

    def singleNumber(self, a1):
        v1, v2 = (0, 0)
        for v3 in a1:
            v1, v2 = (~v3 & v1 | v3 & ~v1 & ~v2, ~v3 & v2 | v3 & v1)
        return v1

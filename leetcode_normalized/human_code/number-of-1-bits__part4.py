class C1(object):

    def hammingWeight(self, a1: int) -> int:
        v1 = '{0:b}'.format(a1)
        v2 = v1.count('1')
        return v2

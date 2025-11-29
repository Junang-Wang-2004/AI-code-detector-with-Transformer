class C1(object):

    def isPowerOfTwo(self, a1):
        return a1 > 0 and a1 & ~-a1 == 0

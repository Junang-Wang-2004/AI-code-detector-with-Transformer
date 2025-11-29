import math

class C1(object):

    def isPowerOfThree(self, a1):
        return a1 > 0 and (math.log10(a1) / math.log10(3)).is_integer()

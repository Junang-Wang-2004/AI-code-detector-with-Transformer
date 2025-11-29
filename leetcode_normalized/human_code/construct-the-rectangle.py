import math

class C1(object):

    def constructRectangle(self, a1):
        """
        """
        v1 = int(math.sqrt(a1))
        while a1 % v1:
            v1 -= 1
        return [a1 // v1, v1]

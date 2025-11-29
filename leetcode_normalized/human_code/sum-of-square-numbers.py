import math

class C1(object):

    def judgeSquareSum(self, a1):
        """
        """
        for v1 in range(int(math.sqrt(a1)) + 1):
            v2 = int(math.sqrt(a1 - v1 ** 2))
            if v1 ** 2 + v2 ** 2 == a1:
                return True
        return False

from functools import reduce

class C1(object):

    def numberCount(self, a1, a2):
        """
        """

        def check(a1):
            v1 = 0
            while a1:
                if v1 & 1 << a1 % 10:
                    return False
                v1 |= 1 << a1 % 10
                a1 //= 10
            return True
        return sum((check(x) for v1 in range(a1, a2 + 1)))

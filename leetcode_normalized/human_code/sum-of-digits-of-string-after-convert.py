from functools import reduce

class C1(object):

    def getLucky(self, a1, a2):
        """
        """
        v1 = reduce(lambda total, x: v1 + sum(divmod(ord(x) - ord('a') + 1, 10)), a1, 0)
        while a2 > 1 and v1 > 9:
            v2 = 0
            while v1:
                v1, v3 = divmod(v1, 10)
                v2 += v3
            v1 = v2
            a2 -= 1
        return v1

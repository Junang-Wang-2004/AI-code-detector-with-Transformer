from functools import reduce

class C1(object):

    def maxLength(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            return reduce(lambda total, x: total + x // a3, a1, 0) >= a2
        v1, v2 = (1, sum(a1) // a2)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2

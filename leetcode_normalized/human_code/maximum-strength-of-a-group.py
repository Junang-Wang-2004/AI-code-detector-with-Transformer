from functools import reduce

class C1(object):

    def maxStrength(self, a1):
        """
        """
        if all((x <= 0 for v1 in a1)) and sum((v1 < 0 for v1 in a1)) <= 1:
            return max(a1)
        v2 = reduce(lambda x, y: v1 * y, (v1 for v1 in a1 if v1))
        return v2 if v2 > 0 else v2 // max((v1 for v1 in a1 if v1 < 0))

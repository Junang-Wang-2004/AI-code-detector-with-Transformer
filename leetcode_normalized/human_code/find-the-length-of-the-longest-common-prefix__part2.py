from functools import reduce

class C1(object):

    def longestCommonPrefix(self, a1, a2):
        """
        """
        v1 = {0}
        for v2 in a1:
            while v2 not in v1:
                v1.add(v2)
                v2 //= 10
        v3 = 0
        for v2 in a2:
            v4 = len(str(v2))
            while v2 not in v1:
                v2 //= 10
                v4 -= 1
            v3 = max(v3, v4)
        return v3

import bisect

class C1(object):

    def findSpecialInteger(self, a1):
        """
        """
        for v1 in [a1[len(a1) // 4], a1[len(a1) // 2], a1[len(a1) * 3 // 4]]:
            if (bisect.bisect_right(a1, v1) - bisect.bisect_left(a1, v1)) * 4 > len(a1):
                return v1
        return -1

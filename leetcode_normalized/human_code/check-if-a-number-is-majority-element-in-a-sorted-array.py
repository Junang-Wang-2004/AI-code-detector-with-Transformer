import bisect

class C1(object):

    def isMajorityElement(self, a1, a2):
        """
        """
        if len(a1) % 2:
            if a1[len(a1) // 2] != a2:
                return False
        elif not a1[len(a1) // 2 - 1] == a1[len(a1) // 2] == a2:
            return False
        v1 = bisect.bisect_left(a1, a2)
        v2 = bisect.bisect_right(a1, a2)
        return (v2 - v1) * 2 > len(a1)

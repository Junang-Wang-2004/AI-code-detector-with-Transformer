import bisect

class C1(object):

    def smallerNumbersThanCurrent(self, a1):
        """
        """
        v1 = sorted(a1)
        return [bisect.bisect_left(v1, i) for v2 in a1]

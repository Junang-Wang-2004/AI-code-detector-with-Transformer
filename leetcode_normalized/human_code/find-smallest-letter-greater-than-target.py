import bisect

class C1(object):

    def nextGreatestLetter(self, a1, a2):
        """
        """
        v1 = bisect.bisect_right(a1, a2)
        return a1[0] if v1 == len(a1) else a1[v1]

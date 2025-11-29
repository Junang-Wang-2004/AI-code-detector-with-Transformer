import itertools

class C1(object):

    def minimumTime(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + (a2 - 1)) // a2
        a1.sort()
        a2.sort()
        return max((ceil_divide(j, w) for v1, v2 in zip(a1, a2)))

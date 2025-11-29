class C1(object):

    def increasingTriplet(self, a1):
        """
        """

        def increasingKUplet(a1, a2):
            v1 = [float('inf')] * (a2 - 1)
            for v2 in a1:
                v3 = bisect.bisect_left(v1, v2)
                if v3 >= a2 - 1:
                    return True
                v1[v3] = v2
            return a2 == 0
        return increasingKUplet(a1, 3)

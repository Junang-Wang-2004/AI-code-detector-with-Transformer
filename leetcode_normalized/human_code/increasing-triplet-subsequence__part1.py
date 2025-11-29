import bisect

class C1(object):

    def increasingTriplet(self, a1):
        """
        """
        v1, v2, v3 = (float('inf'), float('inf'), float('inf'))
        for v4 in a1:
            if v1 >= v4:
                v1 = v4
            elif v3 >= v4:
                v2, v3 = (v1, v4)
            else:
                return True
        return False

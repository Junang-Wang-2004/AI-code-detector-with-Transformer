class C1(object):

    def isReachableAtTime(self, a1, a2, a3, a4, a5):
        """
        """
        v1, v2 = (abs(a1 - a3), abs(a2 - a4))
        v3 = min(v1, v2) + abs(v1 - v2)
        return a5 >= v3 if v3 else a5 != 1

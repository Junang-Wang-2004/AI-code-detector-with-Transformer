class C1(object):

    def maximumPoints(self, a1, a2):
        """
        """
        v1 = min(a1)
        return (a2 - v1 + sum(a1)) // v1 if a2 >= v1 else 0

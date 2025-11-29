class C1(object):

    def distanceTraveled(self, a1, a2):
        """
        """
        v1, v2, v3 = (5, 1, 10)
        v4 = min((a1 - v2) // (v1 - v2), a2)
        return (a1 + v4 * v2) * v3

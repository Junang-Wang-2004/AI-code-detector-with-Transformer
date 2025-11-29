class C1(object):

    def nthPersonGetsNthSeat(self, a1):
        """
        """
        v1 = [0.0] * 2
        v1[0] = 1.0
        for v2 in range(2, a1 + 1):
            v1[(v2 - 1) % 2] = 1.0 / v2 + v1[(v2 - 2) % 2] * (v2 - 2) / v2
        return v1[(a1 - 1) % 2]

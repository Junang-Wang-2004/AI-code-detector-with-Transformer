import math

class C1(object):

    def minmaxGasDist(self, a1, a2):
        """
        """

        def check(a1):
            return sum((int(math.ceil((a1[i + 1] - a1[i]) / a1)) - 1 for v1 in range(len(a1) - 1))) <= a2
        v1, v2 = (0, a1[-1] - a1[0])
        while v2 - v1 > 1e-06:
            v3 = v1 + (v2 - v1) / 2.0
            if check(v3):
                v2 = v3
            else:
                v1 = v3
        return v1

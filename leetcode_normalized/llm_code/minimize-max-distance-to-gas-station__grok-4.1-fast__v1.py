import math

class C1:

    def minmaxGasDist(self, a1, a2):

        def feasible(a1):
            v1 = 0
            for v2 in range(len(a1) - 1):
                v3 = a1[v2 + 1] - a1[v2]
                v1 += math.ceil(v3 / a1) - 1
            return v1 <= a2
        v1, v2 = (0.0, a1[-1] - a1[0])
        for v3 in range(100):
            v4 = (v1 + v2) / 2
            if feasible(v4):
                v2 = v4
            else:
                v1 = v4
        return v1

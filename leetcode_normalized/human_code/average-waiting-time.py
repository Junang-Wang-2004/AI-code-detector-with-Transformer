class C1(object):

    def averageWaitingTime(self, a1):
        """
        """
        v1 = v2 = 0.0
        for v3, v4 in a1:
            v1 = max(v1, v3) + v4
            v2 += v1 - v3
        return v2 / len(a1)

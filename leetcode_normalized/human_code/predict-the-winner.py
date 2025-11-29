class C1(object):

    def PredictTheWinner(self, a1):
        """
        """
        if len(a1) % 2 == 0 or len(a1) == 1:
            return True
        v1 = [0] * len(a1)
        for v2 in reversed(range(len(a1))):
            v1[v2] = a1[v2]
            for v3 in range(v2 + 1, len(a1)):
                v1[v3] = max(a1[v2] - v1[v3], a1[v3] - v1[v3 - 1])
        return v1[-1] >= 0

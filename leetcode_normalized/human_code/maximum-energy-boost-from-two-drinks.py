class C1(object):

    def maxEnergyBoost(self, a1, a2):
        """
        """
        v1 = [0] * 2
        for v2 in range(len(a1)):
            v1 = [max(v1[0] + a1[v2], v1[1]), max(v1[1] + a2[v2], v1[0])]
        return max(v1)

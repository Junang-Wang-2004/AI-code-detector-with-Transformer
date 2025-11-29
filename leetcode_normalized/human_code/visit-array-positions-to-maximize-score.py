class C1(object):

    def maxScore(self, a1, a2):
        """
        """
        v1 = [float('-inf')] * 2
        v1[a1[0] % 2] = a1[0]
        for v2 in range(1, len(a1)):
            v1[a1[v2] % 2] = max(v1[a1[v2] % 2], v1[(a1[v2] + 1) % 2] - a2) + a1[v2]
        return max(v1)

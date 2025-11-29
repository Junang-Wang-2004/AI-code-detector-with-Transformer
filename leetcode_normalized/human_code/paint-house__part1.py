class C1(object):

    def minCost(self, a1):
        """
        """
        if not a1:
            return 0
        v1 = [a1[0], [0, 0, 0]]
        v2 = len(a1)
        for v3 in range(1, v2):
            v1[v3 % 2][0] = a1[v3][0] + min(v1[(v3 - 1) % 2][1], v1[(v3 - 1) % 2][2])
            v1[v3 % 2][1] = a1[v3][1] + min(v1[(v3 - 1) % 2][0], v1[(v3 - 1) % 2][2])
            v1[v3 % 2][2] = a1[v3][2] + min(v1[(v3 - 1) % 2][0], v1[(v3 - 1) % 2][1])
        return min(v1[(v2 - 1) % 2])

class C1(object):

    def maxDotProduct(self, a1, a2):
        """
        """
        if len(a1) < len(a2):
            return self.maxDotProduct(a2, a1)
        v1 = [[0] * len(a2) for v2 in range(2)]
        for v2 in range(len(a1)):
            for v3 in range(len(a2)):
                v1[v2 % 2][v3] = a1[v2] * a2[v3]
                if v2 and v3:
                    v1[v2 % 2][v3] += max(v1[(v2 - 1) % 2][v3 - 1], 0)
                if v2:
                    v1[v2 % 2][v3] = max(v1[v2 % 2][v3], v1[(v2 - 1) % 2][v3])
                if v3:
                    v1[v2 % 2][v3] = max(v1[v2 % 2][v3], v1[v2 % 2][v3 - 1])
        return v1[(len(a1) - 1) % 2][-1]

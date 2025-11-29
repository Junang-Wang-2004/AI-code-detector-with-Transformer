class C1(object):

    def largestTriangleArea(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1) - 2):
            for v3 in range(v2 + 1, len(a1) - 1):
                for v4 in range(v3 + 1, len(a1)):
                    v1 = max(v1, 0.5 * abs(a1[v2][0] * a1[v3][1] + a1[v3][0] * a1[v4][1] + a1[v4][0] * a1[v2][1] - a1[v3][0] * a1[v2][1] - a1[v4][0] * a1[v3][1] - a1[v2][0] * a1[v4][1]))
        return v1

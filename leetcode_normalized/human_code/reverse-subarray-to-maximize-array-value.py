class C1(object):

    def maxValueAfterReverse(self, a1):
        """
        """
        v1, v2, v3, v4 = (0, 0, float('-inf'), float('inf'))
        for v5 in range(1, len(a1)):
            v1 += abs(a1[v5 - 1] - a1[v5])
            v2 = max(v2, abs(a1[0] - a1[v5]) - abs(a1[v5 - 1] - a1[v5]), abs(a1[-1] - a1[v5 - 1]) - abs(a1[v5 - 1] - a1[v5]))
            v4 = min(v4, max(a1[v5 - 1], a1[v5]))
            v3 = max(v3, min(a1[v5 - 1], a1[v5]))
        return v1 + max(v2, (v3 - v4) * 2)

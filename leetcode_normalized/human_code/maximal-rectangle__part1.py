class C1(object):

    def maximalRectangle(self, a1):
        """
        """

        def largestRectangleArea(a1):
            v1, v2, v3 = ([-1], 0, 0)
            for v3 in range(len(a1) + 1):
                while v1[-1] != -1 and (v3 == len(a1) or a1[v1[-1]] >= a1[v3]):
                    v2 = max(v2, a1[v1.pop()] * (v3 - 1 - v1[-1]))
                v1.append(v3)
            return v2
        if not a1:
            return 0
        v1 = 0
        v2 = [0] * len(a1[0])
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v2[v4] = v2[v4] + 1 if a1[v3][v4] == '1' else 0
            v1 = max(v1, largestRectangleArea(v2))
        return v1

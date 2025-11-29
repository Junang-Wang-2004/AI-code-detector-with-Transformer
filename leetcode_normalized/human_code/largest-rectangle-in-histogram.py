class C1(object):

    def largestRectangleArea(self, a1):
        """
        """
        v1, v2 = ([-1], 0)
        for v3 in range(len(a1) + 1):
            while v1[-1] != -1 and (v3 == len(a1) or a1[v1[-1]] >= a1[v3]):
                v2 = max(v2, a1[v1.pop()] * (v3 - 1 - v1[-1]))
            v1.append(v3)
        return v2

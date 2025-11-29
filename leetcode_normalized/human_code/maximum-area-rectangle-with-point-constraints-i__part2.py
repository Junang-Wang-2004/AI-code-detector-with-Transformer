class C1(object):

    def maxRectangleArea(self, a1):
        """
        """
        v1 = -1
        a1.sort()
        for v2 in range(len(a1) - 3):
            if a1[v2][0] != a1[v2 + 1][0]:
                continue
            v3 = next((v3 for v3 in range(v2 + 2, len(a1) - 1) if a1[v2][1] <= a1[v3][1] <= a1[v2 + 1][1]), len(a1) - 1)
            if v3 == len(a1) - 1 or not (a1[v3][0] == a1[v3 + 1][0] and a1[v2][1] == a1[v3][1] and (a1[v2 + 1][1] == a1[v3 + 1][1])):
                continue
            v1 = max(v1, (a1[v2 + 1][1] - a1[v2][1]) * (a1[v3][0] - a1[v2][0]))
        return v1

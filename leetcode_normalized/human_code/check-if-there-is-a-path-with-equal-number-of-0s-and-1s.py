class C1(object):

    def isThereAPath(self, a1):
        """
        """
        if (len(a1) + len(a1[0]) - 1) % 2:
            return False
        v1 = [[float('inf')] * (len(a1[0]) + 1) for v2 in range(2)]
        v1[0][1] = v1[1][0] = 0
        v3 = [[float('-inf')] * (len(a1[0]) + 1) for v2 in range(2)]
        v3[0][1] = v3[1][0] = 0
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v1[(v4 + 1) % 2][v5 + 1] = min(v1[v4 % 2][v5 + 1], v1[(v4 + 1) % 2][v5]) + a1[v4][v5]
                v3[(v4 + 1) % 2][v5 + 1] = max(v3[v4 % 2][v5 + 1], v3[(v4 + 1) % 2][v5]) + a1[v4][v5]
        return v1[len(a1) % 2][-1] <= (len(a1) + len(a1[0]) - 1) // 2 <= v3[len(a1) % 2][-1]

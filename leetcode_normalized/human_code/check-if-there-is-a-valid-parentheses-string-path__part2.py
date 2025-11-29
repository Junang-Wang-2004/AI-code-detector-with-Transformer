class C1(object):

    def hasValidPath(self, a1):
        """
        """
        if (len(a1) + len(a1[0]) - 1) % 2:
            return False
        v1 = [[float('inf'), float('-inf')] for v2 in range(len(a1[0]) + 1)]
        for v3 in range(len(a1)):
            v1[0] = [0, 0] if not v3 else [float('inf'), float('-inf')]
            for v4 in range(len(a1[0])):
                v5 = 1 if a1[v3][v4] == '(' else -1
                v1[v4 + 1] = [min(v1[v4 + 1][0], v1[v4][0]) + v5, max(v1[v4 + 1][1], v1[v4][1]) + v5]
                if v1[v4 + 1][1] < 0:
                    v1[v4 + 1] = [float('inf'), float('-inf')]
                else:
                    v1[v4 + 1][0] = max(v1[v4 + 1][0], v1[v4 + 1][1] % 2)
        return v1[-1][0] == 0

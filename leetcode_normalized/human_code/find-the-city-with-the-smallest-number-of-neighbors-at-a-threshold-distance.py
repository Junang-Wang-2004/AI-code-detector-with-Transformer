class C1(object):

    def findTheCity(self, a1, a2, a3):
        """
        """
        v1 = [[float('inf')] * a1 for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3][v4] = v1[v4][v3] = v5
        for v3 in range(a1):
            v1[v3][v3] = 0
        for v6 in range(a1):
            for v3 in range(a1):
                for v4 in range(a1):
                    v1[v3][v4] = min(v1[v3][v4], v1[v3][v6] + v1[v6][v4])
        v7 = {sum((d <= a3 for v8 in v1[v3])): v3 for v3 in range(a1)}
        return v7[min(v7.keys())]

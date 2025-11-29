class C1(object):

    def maximalRectangle(self, a1):
        """
        """
        if not a1:
            return 0
        v1 = 0
        v2 = len(a1)
        v3 = len(a1[0])
        v4 = [0 for v5 in range(v3)]
        v6 = [0 for v5 in range(v3)]
        v7 = [v3 for v5 in range(v3)]
        for v8 in range(v2):
            v9 = 0
            for v10 in range(v3):
                if a1[v8][v10] == '1':
                    v4[v10] = max(v4[v10], v9)
                    v6[v10] += 1
                else:
                    v4[v10] = 0
                    v6[v10] = 0
                    v7[v10] = v3
                    v9 = v10 + 1
            v11 = v3
            for v10 in reversed(range(v3)):
                if a1[v8][v10] == '1':
                    v7[v10] = min(v7[v10], v11)
                    v1 = max(v1, v6[v10] * (v7[v10] - v4[v10]))
                else:
                    v11 = v10
        return v1

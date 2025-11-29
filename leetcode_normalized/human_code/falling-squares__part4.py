class C1(object):

    def fallingSquares(self, a1):
        """
        """
        v1 = [0] * len(a1)
        for v2 in range(len(a1)):
            v3, v4 = a1[v2]
            v5 = v3 + v4
            v1[v2] += v4
            for v6 in range(v2 + 1, len(a1)):
                v7, v8 = a1[v6]
                v9 = v7 + v8
                if v7 < v5 and v3 < v9:
                    v1[v6] = max(v1[v6], v1[v2])
        v10 = []
        for v11 in v1:
            v10.append(max(v10[-1], v11) if v10 else v11)
        return v10

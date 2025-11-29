class C1:

    def isTransformable(self, a1, a2):
        v1 = [[] for v2 in range(10)]
        for v3, v4 in enumerate(a1):
            v1[int(v4)].append(v3)
        v5 = [0] * 10
        for v4 in a2:
            v6 = int(v4)
            if v5[v6] >= len(v1[v6]):
                return False
            v7 = v1[v6][v5[v6]]
            for v8 in range(v6):
                if v5[v8] < len(v1[v8]) and v1[v8][v5[v8]] < v7:
                    return False
            v5[v6] += 1
        return True

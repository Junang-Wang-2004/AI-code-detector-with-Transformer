class C1:

    def matrixReshape(self, a1, a2, a3):
        if not a1 or a2 * a3 != len(a1) * len(a1[0]):
            return a1
        v1 = [elem for v2 in a1 for v3 in v2]
        v4 = [v1[i * a3:(i + 1) * a3] for v5 in range(a2)]
        return v4

class C1(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = float('inf')
        v2 = 9
        v3 = [0] * (v2 + 1)
        for v4 in range(len(a1[0])):
            v5 = [v1] * (v2 + 1)
            v6 = [0] * (v2 + 1)
            for v7 in range(len(a1)):
                v6[a1[v7][v4]] += 1
            v8 = min(range(v2 + 1), key=lambda x: v3[x])
            v9 = min((v7 for v7 in range(v2 + 1) if v7 != v8), key=lambda x: v3[x])
            for v7 in range(v2 + 1):
                v5[v7] = min(v5[v7], (v3[v8] if v7 != v8 else v3[v9]) + (len(a1) - v6[v7]))
            v3 = v5
        return min(v3)

class C1:

    def minStartingIndex(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        if v2 == 0:
            return 0
        if v1 < v2:
            return -1

        def z_algorithm(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3 = v4 = 0
            for v5 in range(1, v1):
                if v5 < v4:
                    v2[v5] = min(v4 - v5, v2[v5 - v3])
                while v5 + v2[v5] < v1 and a1[v2[v5]] == a1[v5 + v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3 = v5
                    v4 = v5 + v2[v5]
            return v2
        v3 = z_algorithm(a2 + a1)
        v4 = a2[::-1]
        v5 = a1[::-1]
        v6 = z_algorithm(v4 + v5)
        for v7 in range(v1 - v2 + 1):
            v8 = v3[v2 + v7]
            v9 = v6[v1 - v7]
            if v8 + v9 + 1 >= v2:
                return v7
        return -1

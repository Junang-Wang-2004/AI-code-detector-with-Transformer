class C1:

    def longestPrefix(self, a1):

        def compute_z(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3, v4 = (0, 0)
            for v5 in range(1, v1):
                if v5 < v4:
                    v2[v5] = min(v4 - v5, v2[v5 - v3])
                while v5 + v2[v5] < v1 and a1[v2[v5]] == a1[v5 + v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3 = v5
                    v4 = v5 + v2[v5]
            return v2
        v1 = len(a1)
        v2 = compute_z(a1)
        v3 = 0
        for v4 in range(1, v1):
            if v2[v4] >= v1 - v4:
                v3 = max(v3, v1 - v4)
        return a1[:v3]

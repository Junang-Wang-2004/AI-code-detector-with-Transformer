class C1:

    def minimumAverageDifference(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        return min(range(v1), key=lambda k: abs(v2[k + 1] // (k + 1) - (0 if v1 == k + 1 else (v2[v1] - v2[k + 1]) // (v1 - k - 1))))

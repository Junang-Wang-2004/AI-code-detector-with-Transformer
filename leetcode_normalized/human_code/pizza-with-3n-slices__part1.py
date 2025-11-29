class C1(object):

    def maxSizeSlices(self, a1):
        """
        """

        def maxSizeSlicesLinear(a1, a2, a3):
            v1 = [[0] * (len(a1) // 3 + 1) for v2 in range(2)]
            for v3 in range(a2, a3):
                for v4 in reversed(range(1, min((v3 - a2 + 1 - 1) // 2 + 1, len(a1) // 3) + 1)):
                    v1[v3 % 2][v4] = max(v1[(v3 - 1) % 2][v4], v1[(v3 - 2) % 2][v4 - 1] + a1[v3])
            return v1[(a3 - 1) % 2][len(a1) // 3]
        return max(maxSizeSlicesLinear(a1, 0, len(a1) - 1), maxSizeSlicesLinear(a1, 1, len(a1)))

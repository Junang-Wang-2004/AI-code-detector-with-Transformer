class C1(object):

    def maximumSubarrayXor(self, a1, a2):
        """
        """
        v1 = [[a1[i] if j == 0 else 0 for v2 in range(len(a1) - i)] for v3 in range(len(a1))]
        for v3 in reversed(range(len(a1))):
            for v4 in range(1, len(a1) - v3):
                v1[v3][v4] = v1[v3][v4 - 1] ^ v1[v3 + 1][v4 - 1]
        for v3 in reversed(range(len(a1))):
            for v4 in range(1, len(a1) - v3):
                v1[v3][v4] = max(v1[v3][v4], v1[v3][v4 - 1], v1[v3 + 1][v4 - 1])
        return [v1[v3][v2 - v3] for v3, v2 in a2]

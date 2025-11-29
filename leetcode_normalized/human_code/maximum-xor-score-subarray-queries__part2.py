class C1(object):

    def maximumSubarrayXor(self, a1, a2):
        """
        """
        v1 = [[a1[i] if i == j else 0 for v2 in range(len(a1))] for v3 in range(len(a1))]
        for v3 in reversed(range(len(a1))):
            for v2 in range(v3 + 1, len(a1)):
                v1[v3][v2] = v1[v3][v2 - 1] ^ v1[v3 + 1][v2]
        for v3 in reversed(range(len(a1))):
            for v2 in range(v3 + 1, len(a1)):
                v1[v3][v2] = max(v1[v3][v2], v1[v3][v2 - 1], v1[v3 + 1][v2])
        return [v1[v3][v2] for v3, v2 in a2]

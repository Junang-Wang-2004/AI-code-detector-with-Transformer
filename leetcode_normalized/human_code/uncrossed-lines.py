class C1(object):

    def maxUncrossedLines(self, a1, a2):
        """
        """
        if len(a1) < len(a2):
            return self.maxUncrossedLines(a2, a1)
        v1 = [[0 for v2 in range(len(a2) + 1)] for v2 in range(2)]
        for v3 in range(len(a1)):
            for v4 in range(len(a2)):
                v1[(v3 + 1) % 2][v4 + 1] = max(v1[v3 % 2][v4] + int(a1[v3] == a2[v4]), v1[v3 % 2][v4 + 1], v1[(v3 + 1) % 2][v4])
        return v1[len(a1) % 2][len(a2)]

class C1(object):

    def minDeletionSize(self, a1):
        """
        """
        v1 = 0
        v2 = set(range(len(a1) - 1))
        for v3 in range(len(a1[0])):
            if any((a1[i][v3] > a1[i + 1][v3] for v4 in v2)):
                v1 += 1
            else:
                v2 -= set((v4 for v4 in v2 if a1[v4][v3] < a1[v4 + 1][v3]))
        return v1

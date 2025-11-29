class C1(object):

    def checkPartitioning(self, a1):
        """
        """
        v1 = [[False] * len(a1) for v2 in range(len(a1))]
        for v3 in reversed(range(len(a1))):
            for v4 in range(v3, len(a1)):
                if a1[v3] == a1[v4] and (v4 - v3 < 2 or v1[v3 + 1][v4 - 1]):
                    v1[v3][v4] = True
        for v3 in range(1, len(a1) - 1):
            if not v1[0][v3 - 1]:
                continue
            for v4 in range(v3 + 1, len(a1)):
                if not v1[v4][-1]:
                    continue
                if v1[v3][v4 - 1]:
                    return True
        return False

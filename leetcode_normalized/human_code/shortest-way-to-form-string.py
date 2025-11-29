class C1(object):

    def shortestWay(self, a1, a2):
        """
        """
        v1 = [[None for v2 in range(26)] for v2 in range(len(a1) + 1)]
        v3 = [None] * 26
        for v4 in reversed(range(len(a1))):
            v3[ord(a1[v4]) - ord('a')] = v4 + 1
            v1[v4] = list(v3)
        v5, v6 = (1, 0)
        for v7 in a2:
            v6 = v1[v6][ord(v7) - ord('a')]
            if v6 != None:
                continue
            v5 += 1
            v6 = v1[0][ord(v7) - ord('a')]
            if v6 == None:
                return -1
        return v5

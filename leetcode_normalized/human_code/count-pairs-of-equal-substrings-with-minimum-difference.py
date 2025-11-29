class C1(object):

    def countQuadruples(self, a1, a2):
        """
        """
        v1 = [-1] * 26
        for v2 in reversed(range(len(a1))):
            v1[ord(a1[v2]) - ord('a')] = v2
        v3 = [-1] * 26
        for v2 in range(len(a2)):
            v3[ord(a2[v2]) - ord('a')] = v2
        v4, v5 = (0, float('inf'))
        for v2 in range(26):
            if v1[v2] == -1 or v3[v2] == -1:
                continue
            if v1[v2] - v3[v2] < v5:
                v5 = v1[v2] - v3[v2]
                v4 = 0
            v4 += int(v1[v2] - v3[v2] == v5)
        return v4

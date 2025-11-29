class C1(object):

    def minWindow(self, a1, a2):
        """
        """
        v1 = [[None for v2 in range(26)] for v2 in range(len(a1) + 1)]
        v3 = [None] * 26
        for v4 in reversed(range(len(a1))):
            v3[ord(a1[v4]) - ord('a')] = v4 + 1
            v1[v4] = list(v3)
        v5, v6 = (None, float('inf'))
        for v4 in range(len(a1)):
            if a1[v4] != a2[0]:
                continue
            v7 = v4
            for v8 in a2:
                v7 = v1[v7][ord(v8) - ord('a')]
                if v7 == None:
                    break
            else:
                if v7 - v4 < v6:
                    v5, v6 = (v4, v7 - v4)
        return a1[v5:v5 + v6] if v5 is not None else ''

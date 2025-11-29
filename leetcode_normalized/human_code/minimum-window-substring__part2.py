class C1(object):

    def minWindow(self, a1, a2):
        """
        """
        v1 = [0 for v2 in range(52)]
        v3 = [0 for v2 in range(52)]
        for v4 in a2:
            v3[ord(v4) - ord('a')] += 1
        v2, v5, v6, v7, v8 = (0, 0, 0, float('inf'), 0)
        while v2 < len(a1):
            v1[ord(a1[v2]) - ord('a')] += 1
            if v1[ord(a1[v2]) - ord('a')] <= v3[ord(a1[v2]) - ord('a')]:
                v5 += 1
            if v5 == len(a2):
                while v3[ord(a1[v6]) - ord('a')] == 0 or v1[ord(a1[v6]) - ord('a')] > v3[ord(a1[v6]) - ord('a')]:
                    v1[ord(a1[v6]) - ord('a')] -= 1
                    v6 += 1
                if v7 > v2 - v6 + 1:
                    v7 = v2 - v6 + 1
                    v8 = v6
            v2 += 1
        if v7 == float('inf'):
            return ''
        return a1[v8:v8 + v7]

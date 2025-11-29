class C1(object):

    def longestBalanced(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = [0] * 26
            v4 = v5 = 0
            for v6 in range(v2, len(a1)):
                if v3[ord(a1[v6]) - ord('a')] == 0:
                    v5 += 1
                v3[ord(a1[v6]) - ord('a')] += 1
                v4 = max(v4, v3[ord(a1[v6]) - ord('a')])
                if (v6 - v2 + 1) % v5 == 0 and (v6 - v2 + 1) // v5 == v4:
                    v1 = max(v1, v6 - v2 + 1)
        return v1

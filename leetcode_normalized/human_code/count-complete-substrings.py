class C1(object):

    def countCompleteSubstrings(self, a1, a2):
        """
        """
        v1 = v2 = 0
        v3 = [0] * 26
        for v4 in range(1, len(set(a1)) + 1):
            v5 = 0
            for v6 in range(len(a1)):
                v3[ord(a1[v6]) - ord('a')] += 1
                v7 = v3[ord(a1[v6]) - ord('a')]
                v2 += 1 if v7 == a2 else -1 if v7 == a2 + 1 else 0
                if v6 - v5 + 1 == v4 * a2 + 1:
                    v7 = v3[ord(a1[v5]) - ord('a')]
                    v2 -= 1 if v7 == a2 else -1 if v7 == a2 + 1 else 0
                    v3[ord(a1[v5]) - ord('a')] -= 1
                    v5 += 1
                if v2 == v4:
                    v1 += 1
                if v6 + 1 == len(a1) or abs(ord(a1[v6 + 1]) - ord(a1[v6])) > 2:
                    while v5 < v6 + 1:
                        v7 = v3[ord(a1[v5]) - ord('a')]
                        v2 -= 1 if v7 == a2 else -1 if v7 == a2 + 1 else 0
                        v3[ord(a1[v5]) - ord('a')] -= 1
                        v5 += 1
        return v1

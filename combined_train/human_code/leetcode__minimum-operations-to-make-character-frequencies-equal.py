class C1(object):

    def makeStringGood(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = len(a1)
        for v4 in range(min((v2 for v2 in v1 if v2)), max(v1) + 1):
            v5 = v6 = 0
            for v7 in range(26):
                if not v1[v7]:
                    continue
                if v1[v7] >= v4:
                    v8 = len(a1)
                    v9 = min(v5, v6) + (v1[v7] - v4)
                else:
                    v10 = (v1[v7 - 1] - v4 if v1[v7 - 1] >= v4 else v1[v7 - 1]) if v7 - 1 >= 0 else 0
                    v8 = min(min(v5, v6) + (v4 - v1[v7]), v6 + max(v4 - v1[v7] - v10, 0))
                    v9 = min(v5, v6) + v1[v7]
                v5, v6 = (v8, v9)
            v3 = min(v3, v5, v6)
        return v3

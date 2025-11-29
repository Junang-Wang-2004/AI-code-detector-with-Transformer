class C1(object):

    def maximumLength(self, a1):
        """
        """
        v1 = [[0] * 3 for v2 in range(26)]
        v3 = v4 = 0
        for v5, v6 in enumerate(a1):
            v4 += 1
            if v5 + 1 != len(a1) and a1[v5 + 1] == a1[v5]:
                continue
            v7 = v1[ord(v6) - ord('a')]
            for v8 in range(len(v7)):
                if v7[v8] < v4:
                    v4, v7[v8] = (v7[v8], v4)
            v4 = 0
            v3 = max(v3, max(v7[0] - 2, min(v7[0] - 1, v7[1]), v7[2]))
        return v3 if v3 else -1

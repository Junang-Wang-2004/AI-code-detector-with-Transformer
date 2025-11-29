class C1(object):

    def longestBalanced(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = 0
            v4 = set()
            for v5 in range(v2, len(a1)):
                if a1[v5] not in v4:
                    v4.add(a1[v5])
                    v3 += 1 if a1[v5] & 1 else -1
                if v3 == 0:
                    v1 = max(v1, v5 - v2 + 1)
        return v1

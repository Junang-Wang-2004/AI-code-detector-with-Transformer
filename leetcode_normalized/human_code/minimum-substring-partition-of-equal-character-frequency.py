class C1(object):

    def minimumSubstringsInPartition(self, a1):
        """
        """
        v1 = float('inf')
        v2 = [v1] * (len(a1) + 1)
        v2[0] = 0
        for v3 in range(len(a1)):
            v4 = [0] * 26
            v5 = v6 = 0
            for v7 in reversed(range(v3 + 1)):
                v8 = ord(a1[v7]) - ord('a')
                if v4[v8] == 0:
                    v5 += 1
                v4[v8] += 1
                v6 = max(v6, v4[v8])
                if v5 * v6 == v3 - v7 + 1:
                    v2[v3 + 1] = min(v2[v3 + 1], v2[v7] + 1)
        return v2[-1]

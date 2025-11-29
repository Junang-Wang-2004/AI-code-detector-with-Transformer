class C1(object):

    def minSumOfLengths(self, a1, a2):
        """
        """
        v1, v2 = ({0: -1}, [0] * len(a1))
        v3 = v4 = float('inf')
        v5 = 0
        for v6 in range(len(a1)):
            v5 += a1[v6]
            v1[v5] = v6
            if v5 - a2 in v1:
                v7 = v1[v5 - a2]
                v4 = min(v4, v6 - v7)
                if v7 != -1:
                    v3 = min(v3, v2[v7] + (v6 - v7))
            v2[v6] = v4
        return v3 if v3 != float('inf') else -1

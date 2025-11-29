class C1(object):

    def longestCommomSubsequence(self, a1):
        """
        """
        v1 = min(a1, key=lambda x: len(x))
        for v2 in a1:
            v3 = []
            v4, v5 = (0, 0)
            while v4 != len(v1) and v5 != len(v2):
                if v1[v4] < v2[v5]:
                    v4 += 1
                elif v1[v4] > v2[v5]:
                    v5 += 1
                else:
                    v3.append(v1[v4])
                    v4 += 1
                    v5 += 1
            v1 = v3
        return v1

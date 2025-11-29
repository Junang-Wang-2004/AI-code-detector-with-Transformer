class C1(object):

    def maxSubarrays(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v3, v4 = (v3 - 1, v4 - 1)
            if v3 > v4:
                v3, v4 = (v4, v3)
            v1[v4].append(v3)
        v5 = 0
        v6 = [-1] * 2
        v7 = [0] * a1
        for v4 in range(a1):
            for v3 in v1[v4]:
                for v8 in range(len(v6)):
                    if v3 > v6[v8]:
                        v3, v6[v8] = (v6[v8], v3)
            v5 += v4 - v6[0]
            if v6[0] != -1:
                v7[v6[0]] += v6[0] - v6[1]
        return v5 + max(v7)

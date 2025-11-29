class C1(object):

    def maxSum(self, a1, a2, a3):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = [float('-inf')] * (len(a1) + 1)
        v3[0] = 0
        for v2 in range(1, a2 + 1):
            v4 = [float('-inf')] * (len(a1) + 1)
            v5 = float('-inf')
            for v6 in range(v2 * a3 - 1, len(a1)):
                v5 = max(v5, v3[v6 + 1 - a3])
                v4[v6 + 1] = v1[v6 + 1] - v1[v6 + 1 - a3] + v5
                if v6 + 1 != v2 * a3:
                    v4[v6 + 1] = max(v4[v6 + 1], v4[v6] + a1[v6])
            v3 = v4
        return max(v3)

class C1(object):

    def maxSumOfThreeSubarrays(self, a1, a2):
        """
        """
        v1 = len(a1)
        v2 = [0]
        for v3 in a1:
            v2.append(v2[-1] + v3)
        v4 = [0] * v1
        v5 = v2[a2] - v2[0]
        for v6 in range(a2, v1):
            if v2[v6 + 1] - v2[v6 + 1 - a2] > v5:
                v4[v6] = v6 + 1 - a2
                v5 = v2[v6 + 1] - v2[v6 + 1 - a2]
            else:
                v4[v6] = v4[v6 - 1]
        v7 = [v1 - a2] * v1
        v5 = v2[v1] - v2[v1 - a2]
        for v6 in reversed(range(v1 - a2)):
            if v2[v6 + a2] - v2[v6] > v5:
                v7[v6] = v6
                v5 = v2[v6 + a2] - v2[v6]
            else:
                v7[v6] = v7[v6 + 1]
        v8, v9 = ([], 0)
        for v6 in range(a2, v1 - 2 * a2 + 1):
            v10, v11 = (v4[v6 - 1], v7[v6 + a2])
            v5 = v2[v6 + a2] - v2[v6] + (v2[v10 + a2] - v2[v10]) + (v2[v11 + a2] - v2[v11])
            if v5 > v9:
                v9 = v5
                v8 = [v10, v6, v11]
        return v8

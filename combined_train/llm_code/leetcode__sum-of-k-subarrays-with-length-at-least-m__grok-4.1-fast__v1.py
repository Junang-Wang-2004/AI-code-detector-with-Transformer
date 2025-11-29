class C1(object):

    def maxSum(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [0] * (v1 + 1)
        for v5 in range(a2):
            v6 = [float('-inf')] * (v1 + 1)
            v7 = float('-inf')
            v8 = -1
            for v9 in range(1, v1 + 1):
                v6[v9] = v6[v9 - 1]
                if v9 >= a3:
                    while v8 < v9 - a3:
                        v8 += 1
                        v7 = max(v7, v4[v8] - v2[v8])
                    v6[v9] = max(v6[v9], v2[v9] + v7)
            v4 = v6
        return max(v4)

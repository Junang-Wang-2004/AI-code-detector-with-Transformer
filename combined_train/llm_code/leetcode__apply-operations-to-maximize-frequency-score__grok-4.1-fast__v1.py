class C1(object):

    def maxFrequencyScore(self, a1, a2):
        a1.sort()
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]

        def get_cost(a1, a2):
            v1 = a2 - a1 + 1
            v2 = a1 + v1 // 2
            v3 = a1 + (v1 + 1) // 2
            v4 = v2[v2] - v2[a1]
            v5 = v2[a2 + 1] - v2[v3]
            return v5 - v4
        v4 = 0
        v5 = 0
        for v6 in range(v1):
            while v4 <= v6 and get_cost(v4, v6) > a2:
                v4 += 1
            v5 = max(v5, v6 - v4 + 1)
        return v5

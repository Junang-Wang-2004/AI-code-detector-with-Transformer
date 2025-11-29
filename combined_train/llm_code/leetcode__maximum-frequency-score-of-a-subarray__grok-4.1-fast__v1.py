import collections

class C1:

    def maxFrequencyScore(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        if a2 > v2:
            return 0
        v3 = collections.defaultdict(int)
        v4 = 0
        for v5 in range(a2):
            v6 = a1[v5]
            if v3[v6] > 0:
                v4 = (v4 - pow(v6, v3[v6], v1) + v1) % v1
            v3[v6] += 1
            v4 = (v4 + pow(v6, v3[v6], v1)) % v1
        v7 = v4
        for v5 in range(a2, v2):
            v8 = a1[v5 - a2]
            v4 = (v4 - pow(v8, v3[v8], v1) + v1) % v1
            v3[v8] -= 1
            if v3[v8] > 0:
                v4 = (v4 + pow(v8, v3[v8], v1)) % v1
            v9 = a1[v5]
            if v3[v9] > 0:
                v4 = (v4 - pow(v9, v3[v9], v1) + v1) % v1
            v3[v9] += 1
            v4 = (v4 + pow(v9, v3[v9], v1)) % v1
            v7 = max(v7, v4)
        return v7

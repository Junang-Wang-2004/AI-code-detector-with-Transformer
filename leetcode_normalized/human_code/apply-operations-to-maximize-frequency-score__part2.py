class C1(object):

    def maxFrequencyScore(self, a1, a2):
        """
        """
        a1.sort()
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            v3 += a1[v4] - a1[(v2 + v4) // 2]
            while not v3 <= a2:
                v3 -= a1[(v2 + 1 + v4) // 2] - a1[v2]
                v2 += 1
            v1 = max(v1, v4 - v2 + 1)
        return v1

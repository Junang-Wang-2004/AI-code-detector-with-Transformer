class C1(object):

    def maxFrequencyScore(self, a1, a2):
        """
        """

        def check(a1):
            return any((prefix[i + a1] - prefix[i + (a1 + 1) // 2] - (prefix[i + a1 // 2] - prefix[i]) <= a2 for v1 in range(len(a1) - a1 + 1)))
        a1.sort()
        v1 = [0] * (len(a1) + 1)
        for v2, v3 in enumerate(a1):
            v1[v2 + 1] = v1[v2] + v3
        v4, v5 = (1, len(a1))
        while v4 <= v5:
            v6 = v4 + (v5 - v4) // 2
            if not check(v6):
                v5 = v6 - 1
            else:
                v4 = v6 + 1
        return v5

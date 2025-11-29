import bisect

class C1(object):

    def maximumScore(self, a1, a2):
        """
        """

        def score(a1, a2):
            v1 = [a1[a2]] * (a2 + 1)
            for v2 in reversed(range(a2)):
                v1[v2] = min(v1[v2 + 1], a1[v2])
            v3 = v4 = a1[a2]
            for v5 in range(a2 + 1, len(a1)):
                v4 = min(v4, a1[v5])
                v2 = bisect.bisect_left(v1, v4)
                if v2 >= 0:
                    v3 = max(v3, v4 * (v5 - v2 + 1))
            return v3
        return max(score(a1, a2), score(a1[::-1], len(a1) - 1 - a2))

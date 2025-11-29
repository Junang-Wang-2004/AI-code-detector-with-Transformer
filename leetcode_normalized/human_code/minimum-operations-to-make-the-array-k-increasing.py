import bisect

class C1(object):

    def kIncreasing(self, a1, a2):
        """
        """

        def longest_non_decreasing_subsequence(a1):
            v1 = []
            for v2 in a1:
                v3 = bisect.bisect_right(v1, v2)
                if v3 == len(v1):
                    v1.append(v2)
                else:
                    v1[v3] = v2
            return len(v1)
        return len(a1) - sum((longest_non_decreasing_subsequence((a1[j] for v1 in range(i, len(a1), a2))) for v2 in range(a2)))

import bisect

class C1(object):

    def maxPathLength(self, a1, a2):
        """
        """

        def longest_increasing_subsequence(a1):
            v1 = []
            for v2 in a1:
                v3 = bisect.bisect_left(v1, v2)
                if v3 == len(v1):
                    v1.append(v2)
                else:
                    v1[v3] = v2
            return len(v1)
        v1 = a1[a2]
        a1.sort(key=lambda x: (x[0], -x[1]))
        v2, v3 = ([], [])
        for v4, v5 in a1:
            if v4 < v1[0] and v5 < v1[1]:
                v2.append(v5)
            elif v4 > v1[0] and v5 > v1[1]:
                v3.append(v5)
        return longest_increasing_subsequence(v2) + 1 + longest_increasing_subsequence(v3)

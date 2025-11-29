import collections

class C1(object):

    def minimumValueSum(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = (1 << max(a1).bit_length()) - 1

        def memoization(a1, a2, a3):
            if a1 == len(a1) and a2 == len(a2):
                return 0
            if a1 == len(a1) or a2 == len(a2) or a3 < a2[a2]:
                return v1
            if a3 not in lookup[a1][a2]:
                v1 = memoization(a1 + 1, a2, a3 & a1[a1])
                if a3 & a1[a1] == a2[a2]:
                    v1 = min(v1, a1[a1] + memoization(a1 + 1, a2 + 1, v2))
                lookup[a1][a2][a3] = v1
            return lookup[a1][a2][a3]
        v3 = [[collections.defaultdict(int) for v4 in range(len(a2))] for v4 in range(len(a1))]
        v5 = memoization(0, 0, v2)
        return v5 if v5 != v1 else -1

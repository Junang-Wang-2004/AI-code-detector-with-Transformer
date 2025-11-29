import collections

class C1(object):

    def findTargetSumWays(self, a1, a2):
        """
        """

        def subsetSum(a1, a2):
            v1 = collections.defaultdict(int)
            v1[0] = 1
            for v2 in a1:
                for v3 in reversed(range(v2, a2 + 1)):
                    if v3 - v2 in v1:
                        v1[v3] += v1[v3 - v2]
            return v1[a2]
        v1 = sum(a1)
        if v1 < a2 or (a2 + v1) % 2:
            return 0
        v2 = (a2 + v1) // 2
        return subsetSum(a1, v2)

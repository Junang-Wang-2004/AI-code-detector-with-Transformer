import collections

class C1(object):

    def numberOfNodes(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            a2 ^= cnt[a1] % 2
            return a2 + sum((dfs(v, a2) for v2 in range(2 * a1, min(2 * a1 + 1, a1) + 1)))
        v1 = collections.Counter(a2)
        return dfs(1, 0)

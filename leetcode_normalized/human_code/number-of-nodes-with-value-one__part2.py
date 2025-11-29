import collections

class C1(object):

    def numberOfNodes(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = [(1, 0)]
            while v2:
                v3, v4 = v2.pop()
                v4 ^= cnt[v3] % 2
                v1 += v4
                for v5 in reversed(range(2 * v3, min(2 * v3 + 1, a1) + 1)):
                    v2.append((v5, v4))
            return v1
        v1 = collections.Counter(a2)
        return iter_dfs()

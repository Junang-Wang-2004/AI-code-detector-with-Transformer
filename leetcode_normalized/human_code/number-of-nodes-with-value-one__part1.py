import collections

class C1(object):

    def numberOfNodes(self, a1, a2):
        """
        """

        def bfs():
            v1 = 0
            v2 = [(1, 0)]
            while v2:
                v3 = []
                for v4, v5 in v2:
                    v5 ^= cnt[v4] % 2
                    v1 += v5
                    for v6 in range(2 * v4, min(2 * v4 + 1, a1) + 1):
                        v2.append((v6, v5))
                v2 = v3
            return v1
        v1 = collections.Counter(a2)
        return bfs()

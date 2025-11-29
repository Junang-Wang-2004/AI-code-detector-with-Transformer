import collections

class C1(object):

    def countPalindromePaths(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = collections.defaultdict(int)
            v2[0] = 1
            v3 = [(0, 0)]
            while v3:
                v4, v5 = v3.pop()
                if v4:
                    v5 ^= 1 << ord(a2[v4]) - ord('a')
                    v1 += v2[v5] + sum((v2[v5 ^ 1 << i] if v5 ^ 1 << i in v2 else 0 for v6 in range(26)))
                    v2[v5] += 1
                for v7 in reversed(adj[v4]):
                    v3.append((v7, v5))
            return v1
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            if v4 != -1:
                v1[v4].append(v3)
        return iter_dfs()

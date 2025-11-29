import collections

class C1(object):

    def countPalindromePaths(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            v1 = 0
            if a1:
                a2 ^= 1 << ord(a2[a1]) - ord('a')
                v1 += cnt[a2] + sum((cnt[a2 ^ 1 << i] if a2 ^ 1 << i in cnt else 0 for v3 in range(26)))
                cnt[a2] += 1
            return v1 + sum((dfs(v, a2) for v4 in adj[a1]))
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            if v4 != -1:
                v1[v4].append(v3)
        v5 = collections.defaultdict(int)
        v5[0] = 1
        return dfs(0, 0)

# Time:  O(n)
# Space: O(n)
import collections


# dfs, freq table
class Solution2(object):
    def countPalindromePaths(self, parent, s):
        """
        """
        def dfs(u, mask):
            result = 0
            if u:
                mask ^= 1<<(ord(s[u])-ord('a'))
                result += cnt[mask]+sum(cnt[mask^(1<<i)] if mask^(1<<i) in cnt else 0 for i in range(26))
                cnt[mask] += 1
            return result+sum(dfs(v, mask) for v in adj[u])

        adj = [[] for _ in range(len(parent))]
        for u, p in enumerate(parent):
            if p != -1:
                adj[p].append(u)
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        return dfs(0, 0)

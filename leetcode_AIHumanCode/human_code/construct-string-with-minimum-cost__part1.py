# Time:  O(n^2 + w * l)
# Space: O(t)

import itertools
from functools import reduce


# trie, dp
class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        """
        INF = float("inf")
        def query(i):
            curr = trie
            for j in range(i, len(target)):
                x = target[j]
                if x not in curr:
                    break
                curr = curr[x]
                if "_end" in curr:
                    dp[j+1] = min(dp[j+1], dp[i]+curr["_end"])

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for w, c in zip(words, costs):
            node = reduce(dict.__getitem__, w, trie)
            if "_end" not in node:
                node["_end"] = INF
            node["_end"] = min(node["_end"], c)
        dp = [INF]*(len(target)+1)
        dp[0] = 0
        for i in range(len(target)):
            if dp[i] == INF:
                continue
            query(i)
        return dp[-1] if dp[-1] != INF else -1



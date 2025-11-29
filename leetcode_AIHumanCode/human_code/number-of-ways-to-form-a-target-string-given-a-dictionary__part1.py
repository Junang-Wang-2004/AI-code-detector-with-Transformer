# Time:  O(l * (w + n)), l is the length of a word, w is the number of words, n is the length of target
# Space: O(n)

import collections


# optimized from Solution2
class Solution(object):
    def numWays(self, words, target):
        """
        """
        MOD = 10**9+7
        dp = [0]*(len(target)+1)
        dp[0] = 1
        for i in range(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in reversed(range(len(target))):
                dp[j+1] += dp[j]*count[target[j]] % MOD
        return dp[-1] % MOD



# Time:  precompute: O(t + 26)
#        runtime:    O(n)
# Space: O(t + 26)

# precompute, dp
MOD = 10**9+7
MAX_T = 10**5
DP = [0]*(MAX_T+26)
for i in range(26):
    DP[i] = 1
for i in range(26, len(DP)):
    DP[i] = (DP[i-26]+DP[(i-26)+1])%MOD
class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        """
        return reduce(lambda accu, x: (accu+x)%MOD, (DP[((ord(x)-ord('a'))+t)] for x in s), 0)



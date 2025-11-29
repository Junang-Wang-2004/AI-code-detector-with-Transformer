# Time:  O(n^3 * len(diffs)) = O(n^5) at most
# Space: O(n^2 * len(diffs)) = O(n^4) at most
import collections
from functools import reduce


# sort, dp
class Solution2(object):
    def sumOfPowers(self, nums, k):
        """
        """
        MOD = 10**9+7
        nums.sort()
        dp = [[collections.defaultdict(int) for _ in range(len(nums)+1)] for _ in range(len(nums))]        
        for i in range(len(nums)):
            for j in range(max(k-(len(nums)-i+1)-1, 0), i):
                diff = nums[i]-nums[j]
                dp[i][2][diff] += 1
                for l in range(max(k-(len(nums)-i+1), 0), i+1):
                    for mn, cnt in dp[j][l].items():
                        dp[i][l+1][min(diff, mn)] = (dp[i][l+1][min(diff, mn)]+cnt)%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, ((mn*cnt)%MOD for i in range(k-1, len(dp)) for mn, cnt in dp[i][k].items()))

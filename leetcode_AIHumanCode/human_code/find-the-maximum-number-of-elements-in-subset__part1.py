# Time:  O(n)
# Space: O(n)

import collections


# freq table, dp
class Solution(object):
    def maximumLength(self, nums):
        """
        """
        cnt = collections.Counter(nums)
        dp = {}
        result = 0
        for x in cnt.keys():
            if x == 1:
                result = max(result, cnt[x]-(1 if cnt[x]%2 == 0 else 0))
                continue
            stk = []
            while x not in dp and x in cnt and cnt[x] >= 2:
                stk.append(x)
                x *= x
            if x not in dp:
                if x not in cnt:
                    x = stk.pop()
                dp[x] = 1
            l = dp[x]
            while stk:
                l += 2
                dp[stk.pop()] = l
            result = max(result, l)
        return result 
        


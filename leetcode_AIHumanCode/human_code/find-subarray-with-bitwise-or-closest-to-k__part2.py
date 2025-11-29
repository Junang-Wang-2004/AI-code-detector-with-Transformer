# Time:  O(nlogr), r = max(nums)
# Space: O(logr)
# dp, lc1521
class Solution2(object):
    def minimumDifference(self, nums, k):
        """
        """
        result, dp = float("inf"), set()  # at most O(logr) dp states
        for x in nums:
            dp = {x}|{f|x for f in dp}
            for f in dp:
                result = min(result, abs(f-k))
        return result
    

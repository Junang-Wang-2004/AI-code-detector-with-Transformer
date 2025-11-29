# Time:  O(n)
# Space: O(r), r = max(nums)

# freq table
class Solution(object):
    def numberOfPairs(self, nums):
        """
        """
        cnt = [0]*(max(nums)+1)
        pair_cnt = 0
        for x in nums:
            cnt[x] ^= 1
            if not cnt[x]:
                pair_cnt += 1
        return [pair_cnt, len(nums)-2*pair_cnt]



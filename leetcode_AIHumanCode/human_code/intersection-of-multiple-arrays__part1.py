# Time:  O(n * l + r), n = len(nums), l = len(nums[0])
# Space: O(r), r = max(nums)-min(nums)

# freq table, counting sort
class Solution(object):
    def intersection(self, nums):
        """
        """
        MAX_NUM = 1000
        cnt = [0]*(MAX_NUM+1)
        for num in nums:
            for x in num:
                cnt[x] += 1
        return [i for i in range(1, MAX_NUM+1) if cnt[i] == len(nums)]



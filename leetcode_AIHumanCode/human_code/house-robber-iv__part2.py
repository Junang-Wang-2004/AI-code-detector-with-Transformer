# Time:  O(nlogr)
# Space: O(1)
# binary search, greedy
class Solution2(object):
    def minCapability(self, nums, k):
        """
        """
        def check(x):
            cnt = i = 0
            while i < len(nums):
                if nums[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k
    
        left, right = min(nums), max(nums)
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left

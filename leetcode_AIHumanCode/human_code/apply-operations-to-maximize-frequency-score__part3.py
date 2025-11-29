# Time:  O(nlogn)
# Space: O(n)
# sort, prefix sum, binary search
class Solution3(object):
    def maxFrequencyScore(self, nums, k):
        """
        """
        def check(l):
            # "-+ " or "-0+"
            return any((prefix[i+l]-prefix[i+(l+1)//2])-(prefix[i+l//2]-prefix[i]) <= k for i in range(len(nums)-l+1))

        nums.sort()
        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        left, right = 1, len(nums)
        while left <= right:
            mid = left+(right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right

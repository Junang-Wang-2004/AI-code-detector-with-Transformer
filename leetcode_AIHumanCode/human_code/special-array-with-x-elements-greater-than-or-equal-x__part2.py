# Time:  O(n)
# Space: O(1)
# counting sort + binary search solution
class Solution2(object):
    def specialArray(self, nums):
        """
        """
        MAX_NUM = 1000
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            count = [0]*(MAX_NUM+1)
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(range(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in range(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()
    
        inplace_counting_sort(nums, reverse=True)
        left, right = 0, len(nums)-1
        while left <= right:  # Time: O(logn)
            mid = left + (right-left)//2
            if nums[mid] <= mid:
                right = mid-1
            else:
                left = mid+1
        return -1 if left < len(nums) and nums[left] == left else left



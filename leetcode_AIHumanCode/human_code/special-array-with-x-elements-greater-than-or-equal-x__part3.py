# Time:  O(n)
# Space: O(n)
# counting sort + binary search solution
class Solution3(object):
    def specialArray(self, nums):
        """
        """
        MAX_NUM = 1000
        def counting_sort(nums, reverse=False):  # Time: O(n), Space: O(n)
            count = [0]*(MAX_NUM+1)
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            result = [0]*len(nums)
            if not reverse:
                for num in reversed(nums):  # stable sort
                    count[num] -= 1
                    result[count[num]] = num
            else:
                for num in nums:  # stable sort
                    count[num] -= 1
                    result[count[num]] = num
                result.reverse()
            return result
    
        nums = counting_sort(nums, reverse=True)  # extra O(n) space for stable sort
        left, right = 0, len(nums)-1
        while left <= right:  # Time: O(logn)
            mid = left + (right-left)//2
            if nums[mid] <= mid:
                right = mid-1
            else:
                left = mid+1
        return -1 if left < len(nums) and nums[left] == left else left



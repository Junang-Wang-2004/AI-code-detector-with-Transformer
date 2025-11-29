class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            pivot = (low + high) // 2
            total = 0
            ptr = 0
            size = len(nums)
            for idx in range(size):
                while ptr < size and nums[ptr] <= nums[idx] + pivot:
                    ptr += 1
                total += ptr - idx - 1
            if total >= k:
                high = pivot
            else:
                low = pivot + 1
        return low

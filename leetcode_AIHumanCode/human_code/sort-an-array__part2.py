# Time:  O(nlogn), on average
# Space: O(logn)
import random
# quick sort solution
class Solution2(object):
    def sortArray(self, nums):
        """
        """
        def nth_element(nums, left, n, right, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target):
                i = left
                while i <= right:
                    if compare(nums[i], target):
                        nums[i], nums[left] = nums[left], nums[i]
                        left += 1
                        i += 1
                    elif compare(target, nums[i]):
                        nums[i], nums[right] = nums[right], nums[i]
                        right -= 1
                    else:
                        i += 1
                return left, right

            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx])
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        def quickSort(left, right, nums):
            if left > right:
                return
            mid = left + (right-left)//2
            nth_element(nums, left, mid, right)
            quickSort(left, mid-1, nums)
            quickSort(mid+1, right, nums)

        quickSort(0, len(nums)-1, nums)
        return nums

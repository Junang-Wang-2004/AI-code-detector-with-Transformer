# Time:  O(q * n * t) on average
# Space: O(n + q)
import random


# quick select
class Solution2(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        def compare(a, b):
            for i in range(len(nums[a])-t, len(nums[a])):
                if nums[a][i] < nums[b][i]:
                    return True
                if nums[a][i] > nums[b][i]:
                    return False
            return cmp(a, b) < 0

        result = []
        idxs = list(range(len(nums)))
        for k, t in queries:
            nth_element(idxs, k-1, compare=compare)
            result.append(idxs[k-1])
        return result



# Time:  O(max(m, n) * log(max(m, n)))
# Space: O(1)
# Binary search solution.
class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        """
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        def binary_search(compare, nums, left, right, target):
            while left < right:
                mid = left + (right - left) / 2
                if compare(nums[mid], target):
                    right = mid
                else:
                    left = mid + 1
            return left

        nums1.sort(), nums2.sort()

        res = []
        left = 0
        for i in nums1:
            left = binary_search(lambda x, y: x >= y, nums2, left, len(nums2), i)
            if left != len(nums2) and nums2[left] == i:
                res += i,
                left = binary_search(lambda x, y: x > y, nums2, left, len(nums2), i)

        return res



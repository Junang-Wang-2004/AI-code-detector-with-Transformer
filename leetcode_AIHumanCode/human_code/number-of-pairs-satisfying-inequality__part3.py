# Time:  O(nlogn)
# Space: O(n)
import itertools


# merge sort, two pointers
class Solution3(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        """
        def merge_sort(nums, left, right, result):
            if left == right:
                return
            mid = left+(right-left)//2
            merge_sort(nums, left, mid, result)
            merge_sort(nums, mid+1, right, result)
            r = mid+1
            for l in range(left, mid+1):
                while r < right+1 and nums[l]-nums[r] > diff:
                    r += 1
                result[0] += right-r+1
            tmp = []
            l, r = left, mid+1
            while l < mid+1 or r < right+1:
                if r >= right+1 or (l < mid+1 and nums[l] <= nums[r]):
                    tmp.append(nums[l])
                    l += 1
                else:
                    tmp.append(nums[r])
                    r += 1
            nums[left:right+1] = tmp

        nums = [x-y for x, y in zip(nums1, nums2)]
        result = [0]
        merge_sort(nums, 0, len(nums)-1, result)
        return result[0]

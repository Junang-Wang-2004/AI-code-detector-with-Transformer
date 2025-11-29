# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    def findUnsortedSubarray(self, nums):
        """
        """
        a = sorted(nums) #sort the list
        left, right = 0, len(nums) -1 #define left and right pointer
        while (nums[left] == a[left] or nums[right] == a[right]):
            if right - left <= 1:
                return 0
            if nums[left] == a[left]:
                left += 1
            if nums[right] == a[right]:
                right -= 1
        return right - left + 1


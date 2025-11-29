# Time:  O(nlogn)
# Space: O(1)
# sort solution
class Solution4(object):
    def specialArray(self, nums):
        """
        """
        nums.sort(reverse=True)  # Time: O(nlogn)
        for i in range(len(nums)):  # Time: O(n)
            if nums[i] <= i:
                break
        else:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i

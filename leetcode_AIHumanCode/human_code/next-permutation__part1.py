# Time:  O(n)
# Space: O(1)

class Solution(object):
    def nextPermutation(self, nums):
        """
        """
        k, l = -1, 0
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                k = i
                break
        else:
            nums.reverse()
            return

        for i in reversed(range(k+1, len(nums))):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
        


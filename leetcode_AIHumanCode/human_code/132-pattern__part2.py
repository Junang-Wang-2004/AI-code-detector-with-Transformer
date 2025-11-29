# Time:  O(n^2)
# Space: O(1)
class Solution_TLE(object):
    def find132pattern(self, nums):
        """
        """
        for k in range(len(nums)):
            valid = False
            for j in range(k):
                if nums[j] < nums[k]:
                    valid = True
                elif nums[j] > nums[k]:
                    if valid:
                        return True
        return False

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def areNumbersAscending(self, s):
        """
        """
        nums = [int(x) for x in s.split() if x.isdigit()]
        return all(nums[i] < nums[i+1] for i in range(len(nums)-1))

# Time:  O(n * 2^n)
# Space: O(1)
class Solution3(object):
    def subsets(self, nums):
        """
        """
        return self.subsetsRecu([], sorted(nums))

    def subsetsRecu(self, cur, nums):
        if not nums:
            return [cur]

        return self.subsetsRecu(cur, nums[1:]) + self.subsetsRecu(cur + [nums[0]], nums[1:])



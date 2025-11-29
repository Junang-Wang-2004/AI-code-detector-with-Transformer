# Time:  O(n)
# Space: O(1)

# simulation, optimized from solution2
class Solution(object):
    def minMaxGame(self, nums):
        """
        """
        n = len(nums)
        while n != 1:
            new_q = []
            for i in range(n//2):
                nums[i] = min(nums[2*i], nums[2*i+1]) if i%2 == 0 else max(nums[2*i], nums[2*i+1])
            n //= 2
        return nums[0]



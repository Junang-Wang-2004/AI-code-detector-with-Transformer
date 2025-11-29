# Time:  O(n)
# Space: O(1)
class Solution3(object):
    def findErrorNums(self, nums):
        """
        """
        N = len(nums)
        x_minus_y = sum(nums) - N*(N+1)//2
        x_plus_y = (sum(x*x for x in nums) - N*(N+1)*(2*N+1)/6) // x_minus_y
        return (x_plus_y+x_minus_y) // 2, (x_plus_y-x_minus_y) // 2


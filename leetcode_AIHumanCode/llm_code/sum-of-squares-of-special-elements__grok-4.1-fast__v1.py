class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        divs = set()
        lim = int(n ** 0.5) + 1
        for x in range(1, lim):
            if n % x == 0:
                divs.add(x)
                divs.add(n // x)
        return sum(nums[d - 1] * nums[d - 1] for d in divs)

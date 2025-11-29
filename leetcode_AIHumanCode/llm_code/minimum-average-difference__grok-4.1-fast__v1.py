class Solution:
    def minimumAverageDifference(self, nums):
        length = len(nums)
        cum = [0] * (length + 1)
        for j in range(length):
            cum[j + 1] = cum[j] + nums[j]
        return min(range(length), key=lambda k: abs(
            cum[k + 1] // (k + 1) -
            (0 if length == k + 1 else (cum[length] - cum[k + 1]) // (length - k - 1))
        ))

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        freq = [0] * 101
        for val in nums:
            freq[val] += 1
        prefix = [0] * 101
        prefix[0] = freq[0]
        for i in range(1, 101):
            prefix[i] = prefix[i - 1] + freq[i]
        result = []
        for val in nums:
            result.append(prefix[val] - freq[val])
        return result

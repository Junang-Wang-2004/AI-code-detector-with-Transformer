class Solution:
    def findMaxLength(self, nums):
        longest = 0
        balance = 0
        first_occurrence = {0: -1}
        for idx in range(len(nums)):
            balance += 2 * nums[idx] - 1
            if balance not in first_occurrence:
                first_occurrence[balance] = idx
            longest = max(longest, idx - first_occurrence[balance])
        return longest

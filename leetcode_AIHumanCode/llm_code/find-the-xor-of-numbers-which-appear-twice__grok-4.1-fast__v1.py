class Solution:
    def duplicateNumbersXOR(self, nums):
        freq = {}
        for val in nums:
            freq[val] = freq.get(val, 0) + 1
        ans = 0
        for val, cnt in freq.items():
            if cnt == 2:
                ans ^= val
        return ans

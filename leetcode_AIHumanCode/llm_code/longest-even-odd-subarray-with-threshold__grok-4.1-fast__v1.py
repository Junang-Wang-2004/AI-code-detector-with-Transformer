class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        max_len = 0
        curr_len = 0
        expected = 0
        for num in nums:
            parity = num % 2
            if num > threshold:
                curr_len = 0
            elif curr_len == 0:
                if parity == 0:
                    curr_len = 1
                    expected = 1
            elif parity == expected:
                curr_len += 1
                expected = 1 - expected
            else:
                if parity == 0:
                    curr_len = 1
                    expected = 1
                else:
                    curr_len = 0
            max_len = max(max_len, curr_len)
        return max_len

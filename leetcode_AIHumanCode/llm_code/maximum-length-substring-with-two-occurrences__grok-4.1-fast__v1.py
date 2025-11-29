class Solution:
    def maximumLengthSubstring(self, s):
        frequencies = [0] * 26
        num_violations = 0
        window_start = 0
        max_length = 0
        for window_end in range(len(s)):
            char_index = ord(s[window_end]) - ord('a')
            if frequencies[char_index] == 2:
                num_violations += 1
            frequencies[char_index] += 1
            while num_violations > 0 and window_start <= window_end:
                left_char_index = ord(s[window_start]) - ord('a')
                frequencies[left_char_index] -= 1
                if frequencies[left_char_index] == 2:
                    num_violations -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length

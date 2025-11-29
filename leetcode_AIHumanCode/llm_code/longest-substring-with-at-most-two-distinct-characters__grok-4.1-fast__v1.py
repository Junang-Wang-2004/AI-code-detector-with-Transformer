class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        freq = {}
        left = 0
        result = 0
        unique_chars = 0
        for right in range(len(s)):
            curr = s[right]
            if freq.get(curr, 0) == 0:
                unique_chars += 1
            freq[curr] = freq.get(curr, 0) + 1
            while unique_chars > 2:
                lchar = s[left]
                freq[lchar] -= 1
                if freq[lchar] == 0:
                    del freq[lchar]
                    unique_chars -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

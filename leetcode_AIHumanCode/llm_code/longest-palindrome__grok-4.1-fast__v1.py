class Solution:
    def longestPalindrome(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        num_odd = sum(v % 2 for v in freq.values())
        return len(s) - max(0, num_odd - 1)

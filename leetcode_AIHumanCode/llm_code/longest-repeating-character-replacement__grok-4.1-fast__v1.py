class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        longest = 0
        mx = 0
        for r in range(len(s)):
            pos = ord(s[r]) - ord('A')
            freq[pos] += 1
            mx = max(mx, freq[pos])
            while r - l + 1 > mx + k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

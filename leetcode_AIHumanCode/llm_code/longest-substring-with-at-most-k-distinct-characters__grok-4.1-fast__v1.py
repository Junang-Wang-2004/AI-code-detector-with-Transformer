class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        freq_map = {}
        begin = 0
        max_win = 0
        for end in range(len(s)):
            ch = s[end]
            freq_map[ch] = freq_map.get(ch, 0) + 1
            while len(freq_map) > k:
                left_ch = s[begin]
                freq_map[left_ch] -= 1
                if freq_map[left_ch] == 0:
                    del freq_map[left_ch]
                begin += 1
            max_win = max(max_win, end - begin + 1)
        return max_win

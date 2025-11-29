class Solution:
    def firstUniqChar(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for pos, char in enumerate(s):
            if freq[char] == 1:
                return pos
        return -1

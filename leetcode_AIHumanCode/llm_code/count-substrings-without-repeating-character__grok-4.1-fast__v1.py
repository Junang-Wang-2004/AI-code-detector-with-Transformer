class Solution:
    def numberOfSpecialSubstrings(self, s):
        total = 0
        begin = 0
        positions = {}
        for pos in range(len(s)):
            ch = s[pos]
            if ch in positions and positions[ch] >= begin:
                begin = positions[ch] + 1
            positions[ch] = pos
            total += pos - begin + 1
        return total
